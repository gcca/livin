import "../components/home.js";
import "../components/locations.js";

class Content extends HTMLElement {
  static get observedAttributes() {
    return ["option"];
  }

  /**
   * @param {string} name
   * @param {string} curr
   * @param {string} value
   */
  attributeChangedCallback(name, curr, value) {
    if (curr == value) {
      return;
    }
    switch (name) {
      case "option":
        this.switchContent(value);
        break;
      default:
        this.innerHTML = "Unknown";
    }
  }

  /**
   * @param {string} option
   */
  switchContent(option) {
    switch (option) {
      case "/home":
        this.setContent("<livin-home></livin-home>", option);
        break;
      case "/locations":
        this.setContent("<livin-locations></livin-locations>", option);
        break;
    }
  }

  /**
   * @param {string} inner
   * @param {string} path
   */
  setContent(inner, path) {
    this.innerHTML = inner;
    history.pushState({}, path, path);
    this.dispatchEvent(new CustomEvent("loaded-option", { detail: path }));
  }
}

customElements.define("livin-content", Content);
