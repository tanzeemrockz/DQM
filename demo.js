const form = document.querySelector("#dqm-query-form");
const input = document.querySelector("#dqm-query");
const output = document.querySelector("#dqm-output");
const status = document.querySelector("#dqm-status");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const query = input.value.trim();
  if (!query) {
    output.textContent = "Enter a query first.";
    return;
  }

  status.textContent = "Querying DQM…";
  output.textContent = "Traversing paths…";

  try {
    const response = await fetch("/api/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "The query failed.");
    }

    output.textContent = data.answer;
    status.textContent = `Brain: ${data.brain_id} · Engine v${data.engine_version}`;
  } catch (error) {
    output.textContent = error.message || "Could not reach DQM.";
    status.textContent = "Request failed";
  }
});