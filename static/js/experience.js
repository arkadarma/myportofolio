const EXPERIENCE_ENDPOINT = "/api/experience/";
const CREATE_EXPERIENCE_ENDPOINT = "/experience/add-ajax/";

const experienceList =
    document.getElementById("experience-list");

const searchForm =
    document.getElementById("experience-search-form");

const searchInput =
    document.getElementById("experience-search-input");

const experienceForm =
    document.getElementById("experience-form");


let searchDebounceTimer;

let experienceAbortController;


/* =========================
   ESCAPE HTML
   ========================= */

function escapeHtml(value) {
    const div = document.createElement("div");

    div.textContent = value ?? "";

    return div.innerHTML;
}


/* =========================
   DISPLAY STATE
   ========================= */

function displayLoading() {
    experienceList.innerHTML = `
        <div class="empty-state">

            <span>...</span>

            <p>
                Loading experience...
            </p>

        </div>
    `;
}


function displayEmpty() {
    experienceList.innerHTML = `
        <div class="empty-state">

            <span>01</span>

            <p>
                Tidak ada experience yang ditemukan.
            </p>

        </div>
    `;
}


function displayError() {
    experienceList.innerHTML = `
        <div class="empty-state">

            <span>!</span>

            <p>
                Gagal memuat data experience.
            </p>

        </div>
    `;
}


/* =========================
   BUILD EXPERIENCE CARD
   ========================= */

function buildExperienceCard(item) {

    const experience = item.fields;

    const experienceId = item.pk;

    const articleElement =
        document.createElement("article");

    articleElement.className =
        "experience-card";


    /* CATEGORY */

    const categoryHtml = `
        <span class="experience-category">
            ${escapeHtml(experience.category)}
        </span>
    `;


    /* STATUS */

    const statusHtml =
        experience.is_ongoing
            ? `
                <span class="experience-status">
                    Sedang berlangsung
                </span>
              `
            : `
                <span class="experience-status experience-done">
                    Selesai
                </span>
              `;


    /* THUMBNAIL */

    const thumbnailHtml =
        experience.thumbnail
            ? `
                <div class="experience-thumbnail">

                    <img
                        src="${escapeHtml(experience.thumbnail)}"
                        alt="${escapeHtml(experience.title)}"
                    >

                </div>
              `
            : "";


    /* EDIT BUTTON */

    const editHtml =
        (IS_SUPERUSER || IS_EDITOR)
            ? `
                <a
                    href="/experience/${experienceId}/edit/"
                    class="button"
                >
                    Edit
                </a>
              `
            : "";


    /* DELETE BUTTON */

    const deleteHtml =
        IS_SUPERUSER
            ? `
                <form
                    method="POST"
                    action="/experience/${experienceId}/delete/"
                    style="display: inline;"
                >

                    <input
                        type="hidden"
                        name="csrfmiddlewaretoken"
                        value="${CSRF_TOKEN}"
                    >

                    <button
                        type="submit"
                        class="button button-danger"
                        onclick="return confirm('Yakin ingin menghapus experience ini?');"
                    >
                        Delete
                    </button>

                </form>
              `
            : "";


    /* CARD CONTENT */

    articleElement.innerHTML = `

        <div class="experience-top">

            ${categoryHtml}

            ${statusHtml}

        </div>


        <h2>
            ${escapeHtml(experience.title)}
        </h2>


        <p class="experience-description">
            ${escapeHtml(experience.description)}
        </p>


        ${thumbnailHtml}


        ${
            editHtml || deleteHtml
                ? `
                    <div class="experience-card-actions">

                        ${editHtml}

                        ${deleteHtml}

                    </div>
                  `
                : ""
        }

    `;


    return articleElement;
}


/* =========================
   FETCH EXPERIENCE
   ========================= */

async function fetchExperiences(searchQuery = "") {

    if (experienceAbortController) {
        experienceAbortController.abort();
    }


    experienceAbortController =
        new AbortController();


    displayLoading();


    try {

        const url =
            `${EXPERIENCE_ENDPOINT}?title=${encodeURIComponent(searchQuery)}`;


        const response =
            await fetch(
                url,
                {
                    headers: {
                        "Accept": "application/json"
                    },

                    signal:
                        experienceAbortController.signal
                }
            );


        if (!response.ok) {

            throw new Error(
                `HTTP error ${response.status}`
            );

        }


        const data =
            await response.json();


        if (data.length === 0) {

            displayEmpty();

            return;

        }


        experienceList.innerHTML = "";


        data.forEach(function(item) {

            const card =
                buildExperienceCard(item);

            experienceList.appendChild(card);

        });


    } catch (error) {

        if (error.name === "AbortError") {
            return;
        }


        console.error(
            "Error loading experiences:",
            error
        );


        displayError();
    }
}


/* =========================
   SEARCH
   ========================= */

function searchExperiences() {

    const query =
        searchInput.value.trim();


    fetchExperiences(query);
}


/* =========================
   DEBOUNCING
   ========================= */

searchInput.addEventListener(
    "input",
    function() {

        clearTimeout(
            searchDebounceTimer
        );


        searchDebounceTimer =
            setTimeout(
                function() {

                    searchExperiences();

                },
                300
            );

    }
);


/* =========================
   SEARCH FORM SUBMIT
   ========================= */

searchForm.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();


        clearTimeout(
            searchDebounceTimer
        );


        searchExperiences();

    }
);


/* =========================
   CREATE EXPERIENCE
   VIA AJAX
   ========================= */

if (experienceForm) {

    experienceForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const submitButton =
                experienceForm.querySelector(
                    'button[type="submit"]'
                );


            submitButton.disabled = true;


            const formData =
                new FormData(
                    experienceForm
                );


            try {

                const response =
                    await fetch(
                        CREATE_EXPERIENCE_ENDPOINT,
                        {
                            method: "POST",

                            body: formData,

                            headers: {
                                "X-CSRFToken":
                                    CSRF_TOKEN,

                                "Accept":
                                    "application/json"
                            }
                        }
                    );


                const data =
                    await response
                        .json()
                        .catch(
                            function() {
                                return {};
                            }
                        );


                /* =========================
                   SUCCESS
                   ========================= */

                if (response.ok) {

                    experienceForm.reset();


                    const modal =
                        document.getElementById(
                            "add-experience-modal"
                        );


                    if (modal) {

                        modal.hidePopover();

                    }


                    if (
                        typeof showToast ===
                        "function"
                    ) {

                        showToast(
                            "Berhasil",
                            data.message ||
                            "Experience berhasil ditambahkan.",
                            "success"
                        );

                    }


                    fetchExperiences(
                        searchInput.value.trim()
                    );


                }


                /* =========================
                   ERROR
                   ========================= */

                else {

                    let errorMessage =
                        data.message ||
                        `Gagal menambahkan experience (${response.status}).`;


                    if (data.errors) {

                        const fieldErrors = [];


                        Object.keys(
                            data.errors
                        ).forEach(
                            function(field) {

                                data.errors[field]
                                    .forEach(
                                        function(error) {

                                            fieldErrors.push(
                                                error.message
                                            );

                                        }
                                    );

                            }
                        );


                        if (
                            fieldErrors.length > 0
                        ) {

                            errorMessage =
                                fieldErrors.join(
                                    " "
                                );

                        }

                    }


                    if (
                        typeof showToast ===
                        "function"
                    ) {

                        showToast(
                            "Gagal menambahkan experience",
                            errorMessage,
                            "error"
                        );

                    }

                }


            } catch (error) {

                console.error(
                    "Error creating experience:",
                    error
                );


                if (
                    typeof showToast ===
                    "function"
                ) {

                    showToast(
                        "Gagal menambahkan experience",
                        "Tidak dapat terhubung ke server. Silakan coba lagi.",
                        "error"
                    );

                }

            } finally {

                submitButton.disabled =
                    false;

            }

        }
    );

}


/* =========================
   INITIAL LOAD
   ========================= */

fetchExperiences();