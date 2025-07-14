document.addEventListener('DOMContentLoaded', () => {
  const tipoLocalSelect = document.getElementById('id_tipo_local');
  const localInternoDiv = document.querySelector('.local-interno');
  const localExternoDiv = document.querySelector('.local-externo');

  function atualizarCamposVisiveis() {
    const tipo = tipoLocalSelect.value;

    if (tipo === 'interno') {
      localInternoDiv.style.display = 'block';
      localExternoDiv.style.display = 'none';
    } else if (tipo === 'externo') {
      localInternoDiv.style.display = 'none';
      localExternoDiv.style.display = 'block';
    } else {
      // Nenhuma seleção ou "Selecione"
      localInternoDiv.style.display = 'none';
      localExternoDiv.style.display = 'none';
    }
  }

  if (tipoLocalSelect) {
    tipoLocalSelect.addEventListener('change', atualizarCamposVisiveis);
    atualizarCamposVisiveis(); // roda ao carregar
  }
});