$(document).ready(function(){

  $(".app .student-questions #hand-raised-question-alert").click(function() {
    $(this).hide();
  });

  barChart();

  $(window).resize(function(){
    barChart();
  });

  function barChart(){
    $('.bar-chart').find('.item-progress').each(function(){
      var itemProgress = $(this),
        itemProgressWidth = $(this).parent().width() * ($(this).data('percent') / 100);
      itemProgress.css('width', itemProgressWidth);
    });
  };
});
