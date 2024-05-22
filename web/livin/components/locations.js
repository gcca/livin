import "./locations/panel.js";
import "./locations/canvas.js";

class Locations extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <div class="block">
        <livin-locations-panel></livin-locations-panel>
      </div>
      <div class="block">
        <livin-locations-canvas mode=""></livin-locations-canvas>
      </div>
    `;
    this.canvas = this.Select("livin-locations-canvas");
  }

  connectedCallback() {
    this.Select("livin-locations-panel").addEventListener(
      "change",
      this.OnModeChange.bind(this)
    );
  }

  OnModeChange(/** @type{CustomEvent} */ evt) {
    this.canvas.setAttribute("mode", evt.detail);
  }

  /** @param {string} selector */
  Select(selector) {
    const el = this.querySelector(selector);
    if (!el) {
      throw new Error(`No match for selector=${selector}`);
    }
    return el;
  }
}

customElements.define("livin-locations", Locations);
