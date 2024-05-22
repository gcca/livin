import "./modal.js";

class LocationCanvas extends HTMLElement {
  static get observedAttributes() {
    return ["mode"];
  }

  constructor() {
    super();
    this.innerHTML = `
      <style>
        canvas {
          border: 1px solid grey;
          background-color: white;
        }

        td {
          height: 30px;
          width: 30px;
          text-align: center;
        }
      </style>

      <div class="columns">

        <div class="column is-two-thirds">
          <canvas width="680" height="600"></canvas>
        </div>

        <div class="column">
          <table></table>
        </div>

      </div>

      <livin-locations-modal></livin-locations-modal>
    `;

    this.nodes = [];
    this.edges = [];
    this.selectedNode = null;
    this.offsetX = this.offsetY = 0;
    this.label_count = 97;

    this.table = this.Select("table");

    /** @type {import('./modal.js').Modal|null} */
    const modal = this.querySelector("livin-locations-modal");
    if (!modal) {
      throw new Error("Cannot find livin locations modal");
    }
    this.modal = modal;

    this.canvas = this.querySelector("canvas");
    if (this.canvas) {
      this.ctx = this.canvas.getContext("2d");
      if (!this.ctx) {
        throw new Error("Cannot get context");
      }
    } else {
      throw new Error("Cannot find canvas");
    }

    this.OnMouseDownEditBound = this.OnMouseDownEdit.bind(this);
    this.OnMouseDownAddBound = this.OnMouseDownAdd.bind(this);
    this.OnMouseDownConnectBound = this.OnMouseDownConnect.bind(this);
    this.OnMouseMoveEditBound = this.OnMouseMoveEdit.bind(this);
    this.OnDblClickEditBound = this.OnDblClickEdit.bind(this);
    this.OnMouseReleaseBound = this.OnMouseRelease.bind(this);
  }

  connectedCallback() {
    this.modal.addEventListener("change", this.OkModal.bind(this));
  }

  attributeChangedCallback() {
    switch (arguments[1]) {
      case "edit":
        this.canvas.removeEventListener("mousedown", this.OnMouseDownEditBound);
        this.canvas.removeEventListener("mousemove", this.OnMouseMoveEditBound);
        this.canvas.removeEventListener("dblclick", this.OnDblClickEditBound);
        this.canvas.removeEventListener("mouseup", this.OnMouseReleaseBound);
        this.canvas.removeEventListener("mouseout", this.OnMouseReleaseBound);
        break;
      case "add":
        this.canvas.removeEventListener("mousedown", this.OnMouseDownAddBound);
        break;
      case "connect":
        this.canvas.removeEventListener(
          "mousedown",
          this.OnMouseDownConnectBound
        );
    }

    switch (arguments[2]) {
      case "edit":
        this.canvas.addEventListener("mousedown", this.OnMouseDownEditBound);
        this.canvas.addEventListener("mousemove", this.OnMouseMoveEditBound);
        this.canvas.addEventListener("dblclick", this.OnDblClickEditBound);
        this.canvas.addEventListener("mouseup", this.OnMouseReleaseBound);
        this.canvas.addEventListener("mouseout", this.OnMouseReleaseBound);
        break;
      case "add":
        this.canvas.addEventListener("mousedown", this.OnMouseDownAddBound);
        break;
      case "connect":
        this.canvas.addEventListener("mousedown", this.OnMouseDownConnectBound);
    }

    if (this.selectedNode) {
      this.selectedNode.bg = "white";
      this.selectedNode = null;
      this.drawGraph();
    }
  }

  /** @param{CustomEvent} evt */
  OkModal(evt) {
    if (this.selectedNode) {
      this.selectedNode.label = evt.detail;
      this.selectedNode = null;
      this.drawGraph();
    }
  }

  /** @param {MouseEvent} evt */
  OnMouseDownEdit(evt) {
    const { offsetX: x, offsetY: y } = evt;
    this.selectedNode = this.FindNode(x, y);
  }

  /** @param {MouseEvent} evt */
  OnMouseDownAdd(evt) {
    const { offsetX: x, offsetY: y } = evt;
    this.nodes.push({
      x,
      y,
      label: String.fromCharCode(this.label_count),
      bg: "white",
    });
    this.label_count++;
    this.drawGraph();
  }

  /** @param {MouseEvent} evt */
  OnMouseDownConnect(evt) {
    const { offsetX: x, offsetY: y } = evt;
    if (this.selectedNode) {
      const target = this.FindNode(x, y);
      if (target) {
        this.edges.push({ from: this.selectedNode, to: target });
      }

      this.selectedNode.bg = "white";
      this.selectedNode = null;
      this.drawGraph();
    } else {
      this.selectedNode = this.FindNode(x, y);
      if (this.selectedNode) {
        this.selectedNode.bg = "red";
        this.drawGraph();
      }
    }
  }

  /** @param {MouseEvent} evt */
  OnMouseMoveEdit(evt) {
    if (this.selectedNode) {
      const { offsetX: x, offsetY: y } = evt;
      this.selectedNode.x = x - this.offsetX;
      this.selectedNode.y = y - this.offsetY;
      this.drawGraph();
    }
  }

  /** @param {MouseEvent} evt */
  OnDblClickEdit(evt) {
    const { offsetX: x, offsetY: y } = evt;
    this.selectedNode = this.FindNode(x, y);
    if (this.selectedNode) {
      this.modal.Open(this.selectedNode.label);
    }
  }

  OnMouseRelease() {
    this.selectedNode = null;
  }

  drawGraph() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.nodes.forEach((node) => this.drawNode(node));
    this.edges.forEach((edge) => this.drawEdge(edge));
    this.UpdateTable();
  }

  /** @param {{x:number, y:number, label:string, bg:string}} node */
  drawNode({ x, y, label, bg }) {
    const ctx = this.ctx;
    ctx.beginPath();

    ctx.arc(x, y, 15, 0, 2 * Math.PI);
    ctx.fillStyle = bg;
    ctx.fill();

    const labelM = ctx.measureText(label);
    const labelX = x - labelM.width / 2;
    const labelY = y + 2;
    ctx.fillStyle = "black";
    ctx.fillText(label, labelX, labelY);

    ctx.stroke();
  }

  /** @param {{from:{x:number, y:number}, to:{x:number, y:number}, label:string}} edge */
  drawEdge(edge) {
    const { from, to } = edge;
    const dx = to.x - from.x;
    const dy = to.y - from.y;
    const di = Math.sqrt(dx * dx + dy * dy);

    const fromX = from.x + (dx / di) * 15;
    const fromY = from.y + (dy / di) * 15;
    const toX = to.x - (dx / di) * 15;
    const toY = to.y - (dy / di) * 15;

    const ctx = this.ctx;
    ctx.fillStyle = "black";
    edge.label = Math.floor(di / 15).toString();
    ctx.fillText(edge.label, (from.x + to.x) / 2 + 2, (from.y + to.y) / 2 - 2);

    ctx.beginPath();
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(toX, toY);
    ctx.stroke();
    this.drawArrow(from, { x: toX, y: toY });
  }

  /**
   * @param {{x:number, y:number}} from
   * @param {{x:number, y:number}} to
   */
  drawArrow(from, to) {
    const arrowLength = 10;
    const arrowAngle = Math.PI / 6;

    const { x: toX, y: toY } = to;
    const angle = Math.atan2(toY - from.y, toX - from.x);

    const arrowFromX = toX - arrowLength * Math.cos(angle - arrowAngle);
    const arrowFromY = toY - arrowLength * Math.sin(angle - arrowAngle);
    const arrowToX = toX - arrowLength * Math.cos(angle + arrowAngle);
    const arrowToY = toY - arrowLength * Math.sin(angle + arrowAngle);

    const ctx = this.ctx;
    ctx.beginPath();
    ctx.moveTo(toX, toY);
    ctx.lineTo(arrowFromX, arrowFromY);
    ctx.lineTo(arrowToX, arrowToY);
    ctx.closePath();
    ctx.fill();
  }

  UpdateTable() {
    const nodes = this.nodes.slice();
    nodes.sort((node) => node.label);

    const html = [];
    html.push("<tr><td></td>");
    html.push(...nodes.map((node) => `<td>${node.label}</td>`));
    html.push("</tr>");

    const edges = this.edges.slice();
    for (const edge of this.edges) {
      this.VirtualEdges(
        edges,
        this.edges.filter((e) => edge != e),
        edge
      );
    }

    for (const from of nodes) {
      html.push(`<tr><td>${from.label}</td>`);

      for (const to of nodes) {
        if (from == to) {
          html.push("<td>0</td>");
          continue;
        }

        const edge = edges.find((edge) => edge.from == from && edge.to == to);
        html.push("<td>");
        html.push(edge ? edge.label : "-");
        html.push("</td>");
      }
      html.push("</tr>");
    }

    this.table.innerHTML = html.join("");
  }

  /**
   * @typedef {{from:Object, to:Object, label:string}} Edge
   * @param {Array<Edge>} virtuals
   * @param {Array<Edge>} edges
   * @param {Edge} root
   */
  VirtualEdges(virtuals, edges, root) {
    for (const edge of edges) {
      if (root.to == edge.from) {
        const label = (parseInt(root.label) + parseInt(edge.label)).toString();
        const virtual = { from: root.from, to: edge.to, label };
        virtuals.push(virtual);
        this.VirtualEdges(virtuals, edges, virtual);
      }
    }
  }

  /** @param {string} selector */
  Select(selector) {
    let el = this.querySelector(selector);
    if (el) {
      return el;
    } else {
      throw new Error(`Cannot find ${selector}`);
    }
  }

  /**
   * @param {number} x
   * @param {number} y
   */
  FindNode(x, y) {
    for (const node of this.nodes) {
      const offsetX = x - node.x;
      const offsetY = y - node.y;
      const dist = Math.sqrt(offsetX ** 2 + offsetY ** 2);
      if (dist < 15) {
        this.offsetX = offsetX;
        this.offsetY = offsetY;
        return node;
      }
    }
  }
}

customElements.define("livin-locations-canvas", LocationCanvas);
