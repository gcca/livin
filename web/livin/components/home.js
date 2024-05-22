class Home extends HTMLElement {
  constructor() {
    super();
    this.innerHTML = `
      <div class="content">
        <h2>Opciones</h2>
        <ul>
          <li>Lugares</li>
          <li>Rutas</li>
        </ul>
      </div>
    `;
  }
}

customElements.define("livin-home", Home)
