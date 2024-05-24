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

function Homepage7() {
            window.location.href = "/homepage7";
}

function Homepage8() {
            window.location.href = "/homepage8";
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
function indisponibilidades() {
    window.location.href = "/criar_indisponiblidades";
}


// script.js

$(document).ready(function() {
    $('.botao-excluir').click(function() {
        var protocolo = $(this).data('protocolo');
        var cidade = $(this).data('cidade');
        var confirmacao = confirm("Deseja excluir a indisponibilidade? Protocolo: " + protocolo + " e Cidade: " + cidade + "?");
        if (confirmacao) {
            // Envia uma solicitação POST para a rota de exclusão com o protocolo
            $.post('/excluir/' + protocolo, function(data) {
                // Redireciona para a página inicial após a exclusão
                window.location.href = "/homepage6";
            });
        }
    });
});


$(document).ready(function(){
    $("#myModal").modal({
        backdrop: 'static', // Impede o fechamento do modal ao clicar fora dele
        show: true
    });

    $(".modal-header .close").click(function(){
        $("#myModal").modal('hide');
    });

    $("#copyButton").click(function(){
        var modalText = ""; // Inicializa a variável para armazenar o texto formatado
        // Itera sobre cada parágrafo dentro do modal
        $("#myModal .modal-body p").each(function(){
            modalText += $(this).text() + "\n"; // Adiciona o texto do parágrafo atual e uma quebra de linha
        });
        navigator.clipboard.writeText(modalText); // Copia o texto para a área de transferência
        alert("Texto copiado com sucesso!"); // Mostra um alerta de confirmação
    });
});
$(document).ready(function() {
      $('#chkPotenciaOnu').change(function() {
        if ($(this).is(":checked")) {
          $('#campoPotenciaOnu').show();
        } else {
          $('#campoPotenciaOnu').hide();
        }
      });

      $('#chkGpon').change(function() {
        if ($(this).is(":checked")) {
          $('#campoGpon').show();
        } else {
          $('#campoGpon').hide();
        }
      });

      $('#chkPPPoE').change(function() {
        if ($(this).is(":checked")) {
          $('#campoPPPoE').show();
        } else {
          $('#campoPPPoE').hide();
        }
      });

      $('#chkPotenciaOlt').change(function() {
        if ($(this).is(":checked")) {
          $('#campoPotenciaOlt').show();
        } else {
          $('#campoPotenciaOlt').hide();
        }
      });

      $('#chkAlarmes').change(function() {
        if ($(this).is(":checked")) {
          $('#campoAlarmes').show();
        } else {
          $('#campoAlarmes').hide();
        }
      });

      $('#chkocorre').change(function() {
        if ($(this).is(":checked")) {
          $('#campoOcorre').show();
        } else {
          $('#campoOcorre').hide();
        }
      });

      $('#chkTemperatura').change(function() {
        if ($(this).is(":checked")) {
          $('#campoTemp').show();
        } else {
          $('#campoTemp').hide();
        }
      });

      $('#chkModelo').change(function() {
        if ($(this).is(":checked")) {
          $('#campoModelo').show();
        } else {
          $('#campoModelo').hide();
        }
      });

      $('#chkOutros').change(function() {
        if ($(this).is(":checked")) {
          $('#campoOutros').show();
        } else {
          $('#campoOutros').hide();
        }
      });
      });





