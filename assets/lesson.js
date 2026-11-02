function mountQuizzes(root = document) {
  root.querySelectorAll("[data-quiz]").forEach((box) => {
    const answer = box.dataset.answer;
    const fb = box.querySelector(".fb");
    box.querySelectorAll("button[data-choice]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const ok = btn.dataset.choice === answer;
        box.querySelectorAll("button[data-choice]").forEach((b) => {
          b.disabled = true;
          b.dataset.state =
            b.dataset.choice === answer ? "right" : b === btn && !ok ? "wrong" : "";
        });
        if (fb) fb.textContent = ok ? box.dataset.ok || "Yes." : box.dataset.no || "Not that one.";
      });
    });
  });
}

function mountCards(root = document) {
  const secs = [...root.querySelectorAll(".deck section.beat")];
  if (!secs.length) return;
  const dots = root.querySelector("#dots");
  const prev = root.querySelector("#prev-card");
  const next = root.querySelector("#next-card");
  const label = root.querySelector("#card-label");
  let i = 0;

  const show = () => {
    secs.forEach((s, n) => s.classList.toggle("active", n === i));
    if (dots) {
      dots.querySelectorAll("i").forEach((d, n) => d.classList.toggle("on", n === i));
    }
    if (prev) prev.disabled = i === 0;
    if (next) next.disabled = i === secs.length - 1;
    if (label) label.textContent = `${i + 1} / ${secs.length}`;
  };

  if (dots) {
    dots.innerHTML = secs.map((_, n) => `<i class="${n === 0 ? "on" : ""}"></i>`).join("");
    dots.querySelectorAll("i").forEach((d, n) => {
      d.style.cursor = "pointer";
      d.addEventListener("click", () => {
        i = n;
        show();
      });
    });
  }
  if (prev) prev.addEventListener("click", () => { i = Math.max(0, i - 1); show(); });
  if (next) next.addEventListener("click", () => { i = Math.min(secs.length - 1, i + 1); show(); });

  document.addEventListener("keydown", (e) => {
    const t = e.target;
    if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable)) return;
    if (e.key === "ArrowRight" || e.key === "n") { i = Math.min(secs.length - 1, i + 1); show(); }
    if (e.key === "ArrowLeft" || e.key === "p") { i = Math.max(0, i - 1); show(); }
  });
  show();
}

function boot() {
  mountQuizzes();
  mountCards();
}
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", boot);
} else {
  boot();
}
