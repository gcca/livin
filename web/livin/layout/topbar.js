class TopBar extends HTMLElement {
  static get observedAttributes() {
    return ["option"];
  }

  constructor() {
    super();
    this.innerHTML = `
      <nav class="navbar has-shadow" role="navigation" aria-label="main navigation">

        <div class="navbar-brand">
          <a class="navbar-item">
            <em>Livin <i class="fa fa-vcard-o" aria-hidden="true"></i></em>
          </a>

          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="topbar">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="topbar" class="navbar-menu">
          <div class="navbar-start">
            <a class="navbar-item" id="option-home">
              Home
            </a>

            <a class="navbar-item" id="option-locations">
              Locations
            </a>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <a class="button is-primary">
                  <em>Sign In</em>
                </a>
                <a class="button is-light">
                  <i class="fa fa-tasks" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>

        </div>
      </nav>`;
    const noob = {
      classList: { remove: () => {}, add: () => {} },
      addEventListener: () => {},
    };
    this.labelMap = {
      "/home": this.getItem("#option-home"),
      "/locations": this.getItem("#option-locations"),
      "/": noob,
      null: noob,
    };
  }

  /**
   * @param {string} name
   * @param {string} curr
   * @param {string} value
   */
  attributeChangedCallback(name, curr, value) {
    if (curr == value) return;
    switch (name) {
      case "option":
        this.itemClassList(curr).remove("is-selected");
        this.itemClassList(value)?.add("is-selected");
        break;
      default:
        throw new Error(`Unknown option ${name} on topbar`);
    }
  }

  itemClassList(/** @type{string} */ name) {
    const item = this.labelMap[name];
    if (item) {
      return item.classList;
    } else {
      throw new Error(`Cannot find ${name} on map`);
    }
  }

  /**
   * @param {string} select
   */
  getItem(select) {
    let item = this.querySelector(select);
    if (item) {
      return item;
    } else {
      throw new Error(`Cannot find item with select=${select}`);
    }
  }

  connectedCallback() {
    for (const [name, item] of Object.entries(this.labelMap)) {
      item.addEventListener("click", () => this.notifySelectedOption(name));
    }
  }

  notifySelectedOption(/** @type{string} */ name) {
    this.dispatchEvent(
      new CustomEvent("selected-option", {
        detail: name,
        bubbles: true,
        composed: true,
      })
    );
  }
}

customElements.define("livin-topbar", TopBar);
