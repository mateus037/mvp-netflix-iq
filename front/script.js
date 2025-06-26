document.getElementById('form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const form = new FormData(e.target);
  const data = Object.fromEntries(form.entries());
  data.release_year = Number(data.release_year);
  data.duration_int = Number(data.duration_int);
  data.title = data.title.trim();

  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById('result').innerText = `Tipo previsto: ${result.prediction}`;

  const container = document.getElementById('recomendacoes');
  if (result.recomendados && result.recomendados.length > 0) {
    const lista = result.recomendados.map(r => `
    <span class="list-group-item badge text-bg-secondary fs-7">
      ${r.title}
    </span>
`).join('');

    container.innerHTML = `
  <ul class="list-group list-group-horizontal flex-wrap mt-3">${lista}</ul>
`;
  }
  else {
    container.innerHTML = `<p>Nenhuma recomendação disponível.</p>`;
  }
});

// document.getElementById('form-recomendacao').addEventListener('submit', async function (e) {
//   e.preventDefault();

//   const form = new FormData(e.target);
//   const titulo = form.get('title');

//   const response = await fetch('http://127.0.0.1:5000/recomendacao', {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({ title: titulo })
//   });

//   const result = await response.json();
//   const container = document.getElementById('recomendacoes');

//   if (result.erro) {
//     container.innerHTML = `<p class="text-danger">${result.erro}</p>`;
//   } else {
//     const lista = result.recomendados.map(r => `
//       <li class="list-group-item bg-dark text-light">
//         <strong>${r.title}</strong> (${r.release_year}) - ${r.type}
//       </li>
//     `).join('');

//     container.innerHTML = `
//       <ul class="list-group list-group-flush mt-3">${lista}</ul>
//     `;
//   }
// });
