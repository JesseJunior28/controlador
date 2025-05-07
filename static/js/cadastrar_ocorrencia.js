document.addEventListener("DOMContentLoaded", function() {
    const tipo = document.getElementById('id_tipo_local');
    const blocoInt = document.getElementById('local_interno');
    const blocoExt = document.getElementById('local_externo');
  
    function toggle() {
      if (tipo.value === 'interno') {
        blocoInt.style.display = 'block';
        blocoExt.style.display = 'none';
      } else if (tipo.value === 'externo') {
        blocoInt.style.display = 'none';
        blocoExt.style.display = 'block';
      } else {
        blocoInt.style.display = blocoExt.style.display = 'none';
      }
    }
  
    tipo.addEventListener('change', toggle);
    toggle();
  });