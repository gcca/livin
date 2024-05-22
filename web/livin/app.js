import "./layout/topbar.js";
import "./layout/content.js";

class LivinApp extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <livin-topbar option="${location.pathname}"></livin-topbar>
      <div class="container mt-5">
        <div class="block">
          <livin-content option="${location.pathname}"></livin-content>
        </div>
      </div>
    `;
  }

  connectedCallback() {
    this.connectCallback(
      "livin-topbar",
      "selected-option",
      evt => this.OnStateAttribute(evt, "livin-content", "option")
    );
    this.connectCallback(
      "livin-content",
      "loaded-option",
      evt => this.OnStateAttribute(evt, "livin-topbar", "option")
    );
  }

  /**
   * @param{string} select
   * @param{string} type
   * @param{function(Event):void} listener
   */
  connectCallback(select, type, listener) {
    let el = this.querySelector(select);
    if (el) {
      el.addEventListener(type, listener);
    } else {
      throw new Error(`Cannot connect ${select}`);
    }
  }

  /**
   * @param{Event} evt
   * @param{String} select
   * @param{String} name
   */
  OnStateAttribute(evt, select, name) {
    if (!(evt instanceof CustomEvent)) {
      throw new Error(`Unexpected event: ${evt.type} - ${evt}`)
    }
    this.stateAttribute(select, name, evt.detail)
  }

  /**
   * @param{String} select
   * @param{String} name
   * @param{String} value
   */
  stateAttribute(select, name, value) {
    let el = this.querySelector(select);
    if (el) {
      el.setAttribute(name, value);
    } else {
      throw new Error(`${select} not found`);
    }
  }
}

customElements.define("livin-app", LivinApp);
