const EXPERIENCE_ENDPOINT = "/api/v1/experiences/";
const experienceList = document.getElementById("experience-list");
const searchForm = document.getElementById("experience-search-form");
const searchInput = document.getElementById("experience-search-input");
const experienceForm = document.getElementById("experience-form");
const experienceModal = document.getElementById("add-experience-modal");
const experienceIdInput = document.getElementById("experience-id");
const modalTitle = document.getElementById("experience-modal-title");
let searchDebounceTimer;
let experienceAbortController;

function getCookie(name) {
    const prefix = `${name}=`;
    const cookie = document.cookie
        .split(";")
        .map((part) => part.trim())
        .find((part) => part.startsWith(prefix));
    return cookie ? decodeURIComponent(cookie.slice(prefix.length)) : "";
}

function notifyApiError(response, data = {}) {
    let message;
    if (response.status === 400) {
        message = Object.entries(data)
            .flatMap(([field, errors]) =>
                (Array.isArray(errors) ? errors : [errors])
                    .map((error) => `${field}: ${error}`))
            .join(" ") || "Periksa kembali data yang dimasukkan.";
    } else if (response.status === 403) {
        message = "Anda tidak memiliki izin untuk melakukan tindakan ini.";
    } else if (response.status === 404) {
        message = "Data experience tidak ditemukan.";
    } else if (response.status >= 500) {
        message = "Terjadi kesalahan pada server. Silakan coba lagi.";
    } else {
        message = data.detail || `Permintaan gagal (${response.status}).`;
    }
    if (typeof showToast === "function") {
        showToast("Permintaan gagal", message, "error");
    }
}

async function apiRequest(url, options = {}) {
    const headers = new Headers(options.headers || {});
    headers.set("Accept", "application/json");
    if (options.method && options.method !== "GET") {
        headers.set("X-CSRFToken", getCookie("csrftoken"));
        if (options.body) headers.set("Content-Type", "application/json");
    }
    let response;
    try {
        response = await fetch(url, { ...options, headers });
    } catch (error) {
        if (error.name === "AbortError") throw error;
        if (typeof showToast === "function") {
            showToast("Koneksi gagal", "Gagal menghubungi server. Periksa koneksi Anda.", "error");
        }
        throw error;
    }
    if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        notifyApiError(response, data);
        const error = new Error(`API request failed: ${response.status}`);
        error.status = response.status;
        throw error;
    }
    if (response.status === 204) return null;
    return response.json();
}

function showLoading() {
    const state = document.createElement("div");
    state.className = "empty-state";
    const label = document.createElement("p");
    label.textContent = "Loading experience...";
    state.append(label);
    experienceList.replaceChildren(state);
}

function showEmpty() {
    const state = document.createElement("div");
    state.className = "empty-state";
    const label = document.createElement("p");
    label.textContent = "Tidak ada experience yang ditemukan.";
    state.append(label);
    experienceList.replaceChildren(state);
}

function showLoadError() {
    const state = document.createElement("div");
    state.className = "empty-state";
    const label = document.createElement("p");
    label.textContent = "Gagal memuat data experience.";
    state.append(label);
    experienceList.replaceChildren(state);
}

function makeAction(label, className, onClick) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = className;
    button.textContent = label;
    button.addEventListener("click", onClick);
    return button;
}

function buildExperienceCard(experience) {
    const article = document.createElement("article");
    article.className = "experience-card";

    const top = document.createElement("div");
    top.className = "experience-top";
    const category = document.createElement("span");
    category.className = "experience-category";
    category.textContent = experience.category;
    const status = document.createElement("span");
    status.className = experience.is_ongoing
        ? "experience-status"
        : "experience-status experience-done";
    status.textContent = experience.is_ongoing ? "Sedang berlangsung" : "Selesai";
    top.append(category, status);

    const title = document.createElement("h2");
    title.textContent = experience.title;
    const description = document.createElement("p");
    description.className = "experience-description";
    description.textContent = experience.description;
    article.append(top, title, description);

    if (experience.thumbnail) {
        const thumbnailUrl = new URL(experience.thumbnail, window.location.href);
        if (["http:", "https:"].includes(thumbnailUrl.protocol)) {
            const wrapper = document.createElement("div");
            wrapper.className = "experience-thumbnail";
            const image = document.createElement("img");
            image.src = thumbnailUrl.href;
            image.alt = experience.title;
            image.loading = "lazy";
            wrapper.append(image);
            article.append(wrapper);
        }
    }

    const actions = document.createElement("div");
    actions.className = "experience-card-actions";
    if (IS_SUPERUSER || IS_EDITOR) {
        actions.append(makeAction("Edit", "button", () => openExperienceEditor(experience)));
    }
    if (IS_SUPERUSER) {
        actions.append(makeAction("Delete", "button button-danger", async () => {
            if (!window.confirm("Yakin ingin menghapus experience ini?")) return;
            try {
                await apiRequest(`${EXPERIENCE_ENDPOINT}${experience.id}/`, { method: "DELETE" });
                await fetchExperiences(searchInput.value.trim());
                if (typeof showToast === "function") showToast("Berhasil", "Experience dihapus.", "success");
            } catch (error) { /* The request helper displays the error. */ }
        }));
    }
    if (IS_AUTHENTICATED) {
        const starButton = makeAction(
            `${experience.is_starred ? "★" : "☆"} ${experience.star_count}`,
            "button",
            async () => {
                try {
                    const updated = await apiRequest(
                        `${EXPERIENCE_ENDPOINT}${experience.id}/star/`,
                        { method: "POST" },
                    );
                    const replacement = buildExperienceCard(updated);
                    article.replaceWith(replacement);
                    if (typeof showToast === "function") {
                        showToast("Berhasil", updated.is_starred ? "Experience diberi star." : "Star dibatalkan.", "success");
                    }
                } catch (error) { /* The request helper displays the error. */ }
            },
        );
        starButton.setAttribute("aria-pressed", String(experience.is_starred));
        starButton.setAttribute("aria-label", `${experience.star_count} star`);
        actions.append(starButton);
    }
    if (actions.childElementCount) article.append(actions);
    return article;
}

async function fetchExperiences(searchQuery = "") {
    if (experienceAbortController) experienceAbortController.abort();
    experienceAbortController = new AbortController();
    showLoading();
    const params = new URLSearchParams();
    if (searchQuery) params.set("title", searchQuery);
    const query = params.toString();
    try {
        const data = await apiRequest(
            `${EXPERIENCE_ENDPOINT}${query ? `?${query}` : ""}`,
            { signal: experienceAbortController.signal },
        );
        if (!data.length) showEmpty();
        else experienceList.replaceChildren(...data.map(buildExperienceCard));
    } catch (error) {
        if (error.name !== "AbortError") showLoadError();
    }
}

function openExperienceEditor(experience = null) {
    if (!experienceForm || !experienceModal) return;
    experienceForm.reset();
    experienceIdInput.value = experience ? experience.id : "";
    modalTitle.textContent = experience ? "Edit Experience" : "Tambah Experience Baru";
    const submit = experienceForm.querySelector('button[type="submit"]');
    submit.textContent = experience ? "Simpan Perubahan" : "Tambah Experience";
    if (experience) {
        for (const field of ["title", "description", "category", "thumbnail", "ended_at"]) {
            const input = experienceForm.elements.namedItem(field);
            if (!input) continue;
            let value = experience[field] ?? "";
            if (field === "ended_at" && value) value = value.slice(0, 16);
            input.value = value;
        }
    }
    experienceModal.showPopover();
}

const addButton = document.getElementById("add-experience-button");
if (addButton && IS_SUPERUSER) addButton.addEventListener("click", () => openExperienceEditor());

searchInput.addEventListener("input", () => {
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => fetchExperiences(searchInput.value.trim()), 300);
});
searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    clearTimeout(searchDebounceTimer);
    fetchExperiences(searchInput.value.trim());
});

if (experienceForm) {
    experienceForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const submit = experienceForm.querySelector('button[type="submit"]');
        submit.disabled = true;
        const formData = new FormData(experienceForm);
        const payload = Object.fromEntries(
            ["title", "description", "category", "thumbnail", "ended_at"]
                .map((field) => [field, formData.get(field)]),
        );
        if (!payload.ended_at) payload.ended_at = null;
        const id = experienceIdInput.value;
        try {
            await apiRequest(id ? `${EXPERIENCE_ENDPOINT}${id}/` : EXPERIENCE_ENDPOINT, {
                method: id ? "PUT" : "POST",
                body: JSON.stringify(payload),
            });
            experienceModal.hidePopover();
            await fetchExperiences(searchInput.value.trim());
            if (typeof showToast === "function") showToast("Berhasil", id ? "Experience diperbarui." : "Experience ditambahkan.", "success");
        } catch (error) { /* The request helper displays the error. */ }
        finally { submit.disabled = false; }
    });
}

fetchExperiences();
