 
  //excluir Ocorrencia
  document.addEventListener('DOMContentLoaded', function () {
    const excluirModal = document.getElementById('excluirModal');
    const excluirForm = excluirModal.querySelector('#excluirForm');
    const osSpan = excluirModal.querySelector('#osExcluir');

    const excluirBotoes = document.querySelectorAll('button[data-bs-target="#excluirModal"]');

    excluirBotoes.forEach(botao => {
      botao.addEventListener('click', function (event) {
        event.preventDefault();

        const ocorrenciaId = botao.getAttribute('data-id');
        const excluirUrl = botao.getAttribute('data-url');

        osSpan.textContent = ocorrenciaId;
        
        excluirForm.action = excluirUrl;

        const modal = new bootstrap.Modal(excluirModal);
        modal.show();
      });
    });

    excluirModal.addEventListener('hidden.bs.modal', function () {
      const backdrop = document.querySelector('.modal-backdrop');
      if (backdrop) {
        backdrop.remove(); 
      }
    });
  });
  // concluir Ocorrencia
  document.addEventListener('DOMContentLoaded', function () {
    const concluirModal = document.getElementById('concluirModal');
    const concluirForm = concluirModal.querySelector('#concluirForm');
    const osConcluirSpan = concluirModal.querySelector('#osConcluir');

    const concluirBotoes = document.querySelectorAll('button[data-bs-target="#concluirModal"]');

    concluirBotoes.forEach(botao => {
      botao.addEventListener('click', function (event) {
        event.preventDefault();

        const ocorrenciaId = botao.getAttribute('data-id');
        const concluirUrl = botao.getAttribute('data-url');

        osConcluirSpan.textContent = ocorrenciaId;
        concluirForm.action = concluirUrl;

        const modal = new bootstrap.Modal(concluirModal);
        modal.show();
      });
    });

    concluirModal.addEventListener('hidden.bs.modal', function () {
      const backdrop = document.querySelector('.modal-backdrop');
      if (backdrop) {
        backdrop.remove(); 
      }
    });
  }); // cancelar Ocorrencia
  document.addEventListener('DOMContentLoaded', function () {
    const cancelarModal = document.getElementById('cancelarModal');
    const cancelarForm = cancelarModal.querySelector('#cancelarForm');
    const osCancelarSpan = cancelarModal.querySelector('#osCancelar');

    const cancelarBotoes = document.querySelectorAll('button[data-bs-target="#cancelarModal"]');

    cancelarBotoes.forEach(botao => {
      botao.addEventListener('click', function (event) {
        event.preventDefault();

        const ocorrenciaId = botao.getAttribute('data-os');
        const cancelarUrl = botao.getAttribute('data-url');

        osCancelarSpan.textContent = ocorrenciaId;
        cancelarForm.action = cancelarUrl;

        const modal = new bootstrap.Modal(cancelarModal);
        modal.show();
      });
    });

    cancelarModal.addEventListener('hidden.bs.modal', function () {
      const backdrop = document.querySelector('.modal-backdrop');
      if (backdrop) {
        backdrop.remove(); 
      }
    });
  });
  // Adicionar Comentário a ocorrência
  document.addEventListener('DOMContentLoaded', function () {
  const comentarioModal = document.getElementById('comentarioModal');
  const comentarioForm  = document.getElementById('comentarioForm');
  const inputOcorrencia = document.getElementById('id_ocorrencia');

  document.querySelectorAll('button[data-bs-target="#comentarioModal"]')
    .forEach(botao => {
      botao.addEventListener('click', function (e) {
        e.preventDefault();
        inputOcorrencia.value = this.getAttribute('data-ocorrencia');
      });
    });

  if (comentarioForm && !comentarioForm.dataset.listenerAdded) {
    comentarioForm.dataset.listenerAdded = 'true';

    comentarioForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const submitButton = this.querySelector('button[type="submit"]');
      submitButton.disabled = true;
      submitButton.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Enviando...';

      const formData = new FormData(this);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrfToken
        }
      })
      .then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          bootstrap.Modal.getInstance(comentarioModal).hide();
          window.location.reload();
        } else {
          alert(data.message || 'Erro ao salvar comentário');
        }
      })
      .catch(err => {
        console.error('Erro:', err);
        alert('Erro ao salvar comentário');
      })
      .finally(() => {
        submitButton.disabled = false;
        submitButton.innerHTML = 'Enviar';
      });
    });
  }
  comentarioModal.addEventListener('hidden.bs.modal', function () {
    comentarioForm.reset();
    const backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) backdrop.remove();
  });
});