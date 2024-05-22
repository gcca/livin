export class Modal extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <div class="modal">

        <div class="modal-background"></div>

        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Editar 📝</p>
            <button class="delete" aria-label="close"></button>
          </header>

          <section class="modal-card-body">
            <div class="field">
              <label class="label">Label</label>
              <div class="control">
                <input class="input" type="text">
              </div>
            </div>
          </section>

        </div>

      </div>
    `;

    this.modal = this.querySelector(".modal");
    if (!this.modal) {
      throw new Error("No modal found");
    }

    this.input = this.querySelector("input");
    if (!this.input) {
      throw new Error("No input found");
    }
  }

  connectedCallback() {
    this.querySelectorAll(
      ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button"
    ).forEach((el) => {
      el.addEventListener("click", this.Close.bind(this));
    });

    this.input.addEventListener("change", (evt) => {
      evt.stopPropagation();
    });

    this.input.addEventListener("keypress", (evt) => {
      if (evt.key == "Enter") {
        this.Ok();
      }

      if (evt.key == "Escape") {
        this.Close();
      }
    });
  }

  /** @param{string} value */
  Open(value) {
    this.input.value = value;
    this.modal.classList.add("is-active");
    this.input.focus();
  }

  Ok() {
    this.dispatchEvent(new CustomEvent("change", { detail: this.input.value }));
    this.Close();
  }

  Close() {
    this.modal.classList.remove("is-active");
  }
}

customElements.define("livin-locations-modal", Modal);
