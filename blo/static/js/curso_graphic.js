// grafico do total de Candidatos 
$(document).ready(function() {
    var url = "/curso_not_js/";

    $.getJSON(url, function(res){
      var data = res.cursos.map(function(v){
        return [v.curso, v.quantidade]
      })  

      Highcharts.setOptions({
        lang: {
          drillUpText: '<< Voltar '
        }
      });
    
      Highcharts.chart('containerNot', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Cursos VG Noturno'
        },
        subtitle: {
          text: 'Quantidade de candidatos por curso'
        },
        xAxis: {
          type: 'category'
        },
        yAxis: {
          title: {
            text: 'Quantidade'
          }
        },
        legend: {
          enabled: false
        },
        plotOptions: {
          series: {
            borderWidth: 1,
            dataLabels: {
              enabled: true,
              format: '{point.y}'
            }
          }
        },
        tooltip: {
          headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
          pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
          // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
        },    
    
        series: [{
          name: 'Curso',
          colorByPoint: true,
  
          data: data
        }],
        // drilldown: {
        //   series: [{
        //       name: 'EAD',
        //       id: 'EAD',
        //       data: [
        //         ['Setembro', 3.0],
        //         ['Outubro', 2.0],
        //       ]
        //     },
        //     {
        //       name: 'Administração',
        //       id: 'Administração',
        //       data: [
        //         ['v40.0', 30.0],
        //         ['v41.0', 20.8],    
        //       ]
        //     }
        //   ]
        // }
      });
    });

    
  });



$(document).ready(function() {
  var url = "/curso_json/";

  $.getJSON(url, function(res){
    var data = res.cursos.map(function(v){
      return [v.curso, v.quantidade]
    })  

    Highcharts.setOptions({
      lang: {
        drillUpText: '<< Voltar '
      }
    });
  
    Highcharts.chart('container', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Cursos VG Matutino'
      },
      subtitle: {
        text: 'Quantidade de candidatos por curso'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        title: {
          text: 'Quantidade'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        series: {
          borderWidth: 1,
          dataLabels: {
            enabled: true,
            format: '{point.y}'
          }
        }
      },
      tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
        // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
      },    
  
      series: [{
        name: 'Curso',
        colorByPoint: true,

        data: data
      }],
    });
  });
// grafico do total de Candidatos 


// grafico do total de Candidatos Confirmados
$(document).ready(function() {
  var url = "/confirm_sala_js";

  $.getJSON(url, function(res){
    var data = res.salas.map(function(v){
      return [v.sala, v.confirmados]
    })  

    Highcharts.setOptions({
      lang: {
        drillUpText: '<< Voltar '
      }
    });
  
    Highcharts.chart('containerS', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Salas'
      },
      subtitle: {
        text: 'Quantidade de candidatos por sala'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        title: {
          text: 'Quantidade'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        series: {
          borderWidth: 1,
          dataLabels: {
            enabled: true,
            format: '{point.y}'
          }
        }
      },
      tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
        // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
      },    
  
      series: [{
        name: 'Sala',
        colorByPoint: true,

        data: data
      }],
    });
  });


});

$(document).ready(function() {
  var url = "/confirm_curM_js";

  $.getJSON(url, function(res){
    var data = res.cursos.map(function(v){
      return [v.curso, v.quantidade]
    })  

    Highcharts.setOptions({
      lang: {
        drillUpText: '<< Voltar '
      }
    });
  
    Highcharts.chart('containerM', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Confirmados Matutino'
      },
      subtitle: {
        text: 'Quantidade de candidatos confirmados por Curso'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        title: {
          text: 'Quantidade'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        series: {
          borderWidth: 1,
          dataLabels: {
            enabled: true,
            format: '{point.y}'
          }
        }
      },
      tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
        // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
      },    
  
      series: [{
        name: 'Curso',
        colorByPoint: true,

        data: data
      }],
    });
  });


});

$(document).ready(function() {
  var url = "/confirm_curN_js";

  $.getJSON(url, function(res){
    var data = res.cursos.map(function(v){
      return [v.curso, v.quantidade]
    })  

    Highcharts.setOptions({
      lang: {
        drillUpText: '<< Voltar '
      }
    });
  
    Highcharts.chart('containerN', {
      chart: {
        type: 'column'
      },
      title: {
        text: 'Confirmados Noturno'
      },
      subtitle: {
        text: 'Quantidade de candidatos confirmados por Curso'
      },
      xAxis: {
        type: 'category'
      },
      yAxis: {
        title: {
          text: 'Quantidade'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        series: {
          borderWidth: 1,
          dataLabels: {
            enabled: true,
            format: '{point.y}'
          }
        }
      },
      tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}</b> do total<br/>'
        // pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> do total<br/>'
      },    
  
      series: [{
        name: 'Curso',
        colorByPoint: true,

        data: data
      }],
    });
  });


});
// grafico do total de Candidatos Confirmados


// grafico de impressão 
  $(document).ready(function(){
    var url = '/print_js'
    $.getJSON(url, function(res){
      var data = res.print.map(function(v){
        return [v.data, v.impresso]
      })  

      Highcharts.chart('containerPA', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false, 
            type: 'pie'
        },

        title: {
            text: 'Comparação de Impressões realizadas no VG'
        },

        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: data
        }]
    });
      
    });

  });

  $(document).ready(function(){
    var url = '/curso_json/'
    $.getJSON(url, function(res){
      var data = res.cursos.map(function(v){
        return [v.curso, v.quantidade]
      })  

      Highcharts.chart('containerP', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false, 
            type: 'pie'
        },

        title: {
            text: 'Browser market shares in January, 2018'
        },

        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
          name: 'Brands',
          colorByPoint: true,
          data: [
            {
              name: 'VG-20/10/2018',
              y: 86.05,
              sliced: true,
              selected: true
            },
            {
            name: 'VG-24/11/2018',
            y: 76.05,
            sliced: true,
            selected: true
            },
            {
            name: 'VG-19/01/2019',
            y: 10.00
            }
          ]

        }]
    });
      
    });

  });


  // grafico de impressão 

  
});
  