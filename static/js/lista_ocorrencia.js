document.addEventListener('DOMContentLoaded', function() {
    // Inicialização dos tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Função para ordenar a tabela
    function sortTable(columnIndex) {
        const table = document.querySelector('.table');
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));

        rows.sort((a, b) => {
            const aValue = a.cells[columnIndex].textContent.trim();
            const bValue = b.cells[columnIndex].textContent.trim();

            // Verifica se os valores são números
            const aNum = parseFloat(aValue);
            const bNum = parseFloat(bValue);

            if (!isNaN(aNum) && !isNaN(bNum)) {
                return aNum - bNum;
            }

            return aValue.localeCompare(bValue);
        });

        // Remove todas as linhas
        while (tbody.firstChild) {
            tbody.removeChild(tbody.firstChild);
        }

        // Adiciona as linhas ordenadas
        rows.forEach(row => tbody.appendChild(row));
    }

    // Adiciona eventos de clique nos cabeçalhos da tabela
    const headers = document.querySelectorAll('.table thead th');
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', () => sortTable(index));
    });

    // Função para filtrar a tabela
    function filterTable() {
        const input = document.getElementById('searchInput');
        const filter = input.value.toUpperCase();
        const table = document.querySelector('.table');
        const tr = table.getElementsByTagName('tr');

        for (let i = 1; i < tr.length; i++) {
            let found = false;
            const td = tr[i].getElementsByTagName('td');
            
            for (let j = 0; j < td.length; j++) {
                if (td[j]) {
                    const txtValue = td[j].textContent || td[j].innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }
            
            tr[i].style.display = found ? '' : 'none';
        }
    }

    // Adiciona campo de busca se não existir
    if (!document.getElementById('searchInput')) {
        const searchContainer = document.createElement('div');
        searchContainer.className = 'mb-3';
        searchContainer.innerHTML = `
            <div class="input-group">
                <span class="input-group-text">
                    <i class="bi bi-search"></i>
                </span>
                <input type="text" id="searchInput" class="form-control" placeholder="Buscar...">
            </div>
        `;
        document.querySelector('.table-responsive').insertBefore(searchContainer, document.querySelector('.table'));
        
        // Adiciona evento de input no campo de busca
        document.getElementById('searchInput').addEventListener('input', filterTable);
    }

    // Função para exportar dados
    function exportToCSV() {
        const table = document.querySelector('.table');
        const rows = table.querySelectorAll('tr');
        let csv = [];

        // Cabeçalhos
        const headers = [];
        table.querySelectorAll('th').forEach(th => {
            headers.push(th.textContent.trim());
        });
        csv.push(headers.join(','));

        // Dados
        rows.forEach(row => {
            if (row.style.display !== 'none') {
                const cells = [];
                row.querySelectorAll('td').forEach(td => {
                    cells.push(td.textContent.trim());
                });
                csv.push(cells.join(','));
            }
        });

        // Cria o arquivo
        const csvContent = csv.join('\n');
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'ocorrencias.csv';
        link.click();
    }

    // Adiciona botão de exportação se não existir
    if (!document.getElementById('exportButton')) {
        const exportButton = document.createElement('button');
        exportButton.id = 'exportButton';
        exportButton.className = 'btn btn-success mb-3';
        exportButton.innerHTML = '<i class="bi bi-download"></i> Exportar CSV';
        exportButton.addEventListener('click', exportToCSV);
        document.querySelector('.table-responsive').insertBefore(exportButton, document.querySelector('.table'));
    }

    // Adiciona confirmação para ações críticas
    document.querySelectorAll('[data-confirm]').forEach(element => {
        element.addEventListener('click', function(e) {
            if (!confirm(this.getAttribute('data-confirm'))) {
                e.preventDefault();
            }
        });
    });

    // Adiciona animação de loading
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processando...';
            }
        });
    });

    // Sistema de notificações
    function checkForUpdates() {
        fetch('/api/ocorrencias/ultimas/')
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    showNotification('Nova ocorrência', 'Uma nova ocorrência foi cadastrada.');
                }
            })
            .catch(error => console.error('Erro ao verificar atualizações:', error));
    }

    function showNotification(title, message) {
        if (!("Notification" in window)) {
            console.log("Este navegador não suporta notificações desktop");
            return;
        }

        if (Notification.permission === "granted") {
            new Notification(title, {
                body: message,
                icon: '/static/img/notification-icon.png'
            });
        } else if (Notification.permission !== "denied") {
            Notification.requestPermission().then(permission => {
                if (permission === "granted") {
                    new Notification(title, {
                        body: message,
                        icon: '/static/img/notification-icon.png'
                    });
                }
            });
        }
    }

    // Verifica atualizações a cada 30 segundos
    setInterval(checkForUpdates, 30000);
}); 