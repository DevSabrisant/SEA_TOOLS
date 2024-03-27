function Home() {
   window.location.href = "/";
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
        tableBody += '<td><input type="date" name="data_' + (i + 1) + '"></td>';
        tableBody += '<td><input type="number" name="valor_' + (i + 1) + '"></td>';
        tableBody += '</tr>';
    }

    document.querySelector("#excelTable tbody").innerHTML = tableBody;
}



