document.addEventListener('DOMContentLoaded', function () {
  const tipoSelect = document.querySelector('select[name="tipo_local"]');
  const localInterno = document.querySelectorAll('.local-interno');
  const localExterno = document.querySelectorAll('.local-externo');

  if (!tipoSelect) return; // Evita erro caso o campo não esteja presente

  function toggleCampos(tipo) {
      if (tipo === 'interno') {
            localInterno.forEach(el => el.style.display = 'block');
            localExterno.forEach(el => el.style.display = 'none');
      } else if (tipo === 'externo') {
            localInterno.forEach(el => el.style.display = 'none');
            localExterno.forEach(el => el.style.display = 'block');
      } else {
            localInterno.forEach(el => el.style.display = 'none');
            localExterno.forEach(el => el.style.display = 'none');
      }
  }

  // Executa ao carregar a página
  toggleCampos(tipoSelect.value);

  // Executa ao mudar o valor do select
  tipoSelect.addEventListener('change', function () {
      toggleCampos(this.value);
  });
});