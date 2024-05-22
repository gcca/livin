import "./mode.js";

class Panel extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <livin-locations-mode></livin-locations-mode>
    `;
  }
}

customElements.define("livin-locations-panel", Panel);
