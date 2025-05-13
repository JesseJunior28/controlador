document.addEventListener("DOMContentLoaded", function () {
    const tipoLocal = document.querySelector("#id_tipo_local");
    const internoFields = document.querySelector(".local-interno");
    const externoFields = document.querySelector(".local-externo");

    // Esconde os campos ao carregar
    function esconderTodos() {
        internoFields.style.display = "none";
        externoFields.style.display = "none";
    }

    // Mostra os campos com base na seleção
    function mostrarCamposCorretos() {
        const valor = tipoLocal.value;

        esconderTodos(); // Esconde tudo antes

        if (valor === "interno") {
            internoFields.style.display = "block";
        } else if (valor === "externo") {
            externoFields.style.display = "block";
        }
    }

    // Esconde tudo no início
    esconderTodos();

    // Ativa ao mudar o tipo de local
    tipoLocal.addEventListener("change", mostrarCamposCorretos);
});