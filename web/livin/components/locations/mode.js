class Mode extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <div class="buttons has-addons">
        <button class="button" data-mode="edit" data-is="is-info">
          <span class="icon is-small"><i class="fa fa-pencil-square-o"></i></span>
          <span>Editar</span>
        </button>
        <button class="button" data-mode="add" data-is="is-success">
          <span class="icon is-small"><i class="fa fa-code-fork"></i></span>
          <span>Agregar</span>
        </button>
        <button class="button" data-mode="connect" data-is="is-warning">
          <span class="icon is-small"><i class="fa fa-plug"></i></span>
          <span>Conectar</span>
        </button>
      </div>
    `;

    this.selected = {
      classList: { remove: (/** @type{Array<string>} */ ..._) => {} },
      dataset: {},
    };

    this.querySelectorAll("button").forEach((btn) =>
      btn.addEventListener("click", this.OnChange.bind(this))
    );
  }

  /** @param {Event} evt */
  OnChange(evt) {
    const target = evt.currentTarget;
    if (target instanceof HTMLButtonElement) {
      const dataset = target.dataset;

      if (!dataset.is) {
        throw new Error("Dataset is not defined");
      }

      this.selected.classList.remove(this.selected.dataset.is, "is-selected");
      target.classList.add(dataset.is, "is-selected");
      this.selected = target;

      this.dispatchEvent(new CustomEvent("change", { detail: dataset.mode, bubbles: true }));
    } else {
      throw new Error("No mode target");
    }
  }
}

customElements.define("livin-locations-mode", Mode);
