function Home() {
   window.location.href = "/";
}

function login() {
   window.location.href = "/login";
}

function copiarTexto() {
   var textarea = document.getElementById('resultado');
   textarea.select();
   document.execCommand('copy');
}

function copiarTexto4() {
   var textarea = document.getElementById('resultado_cancelamento');
   textarea.select();
   document.execCommand('copy');
}

function copiarTexto2() {
            var textarea = document.getElementById('resultadoVencimento');
            textarea.select();
            document.execCommand('copy');
}

function copiarTexto3() {
            var textarea = document.getElementById('resultadoDesc');
            textarea.select();
            document.execCommand('copy');
}

function Homepage() {
            window.location.href = "/homepage";
}

function Homepage2() {
            window.location.href = "/homepage2";
}

function Homepage3(){
            window.location.href = "/homepage3";
}

function Homepage4(){
            window.location.href = "/homepage4";
}

function Homepage5(){
            window.location.href = "/homepage5";
}

function Homepage6() {
            window.location.href = "/homepage6";
}

 function validarFormulario() {
            var dataAti = document.getElementById("data_ati").value;
            var dataSolicitacao = document.getElementById("dataSolicitacao").value;
            var multaCheckbox = document.getElementById("multa");


            if (!dataAti && multaCheckbox.checked) {
                alert("Por favor, preencha o campo Inicio da Fidelidade se a Multa estiver ativada.");
                return false;
            }


            if (dataAti && dataSolicitacao && dataAti > dataSolicitacao && multaCheckbox.checked) {
                alert("A data de Início da Fidelidade não pode ser maior que a Data de Solicitação.");
                return false;
            }
            if (!dataAti && !multaCheckbox.checked) {
                document.getElementById("data_ati").value = "False";
            }

            return true;
        }

function generateTable() {
    var rows = document.getElementById("rows").value;
    var tableBody = '';

    for (var i = 0; i < rows; i++) {
        tableBody += '<tr>';
        tableBody += '<td><input type="date" class="data" name="data_' + (i + 1) + '"></td>';
        tableBody += '<td><input type="text" class="valor" name="valor_' + (i + 1) + '"></td>';
        tableBody += '</tr>';
    }

    document.querySelector("#excelTable tbody").innerHTML = tableBody;
}

function ValidarNegociacao() {
        // Seleciona todos os campos de data e valor
        var camposData = document.querySelectorAll('.data');
        var camposValor = document.querySelectorAll('.valor');

        // Itera sobre os campos de data e valor
        for (var i = 0; i < camposData.length; i++) {
            var data = camposData[i].value;
            var valor = camposValor[i].value;

            // Verifica se os campos estão vazios
            if (data === '' || valor === '') {
                alert('Por favor, preencha todos os campos.');
                return false; // Impede o envio do formulário
            }
        }

        // Se todos os campos estiverem preenchidos, retorna true para permitir o envio do formulário
        return true;
    }
function validarNumero(input) {
        // Remove qualquer caractere que não seja número, vírgula ou ponto
        input.value = input.value.replace(/[^\d,.]/g, '');
}

function logout() {
            window.location.href = "/logout";
        }

