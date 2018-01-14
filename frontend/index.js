function getHoursMinuteFormat(time) {
  // Hours, minutes and seconds
  var hrs = ~~(time / 3600);
  var mins = ~~((time % 3600) / 60);
  var secs = time % 60;

  // Output like "1:01" or "4:03:59" or "123:03:59"
  var ret = "";

  if (hrs > 0) {
    ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
  }

  ret += "" + mins + ":" + (secs < 10 ? "0" : "");
  ret += "" + secs;
  return ret;
}

$(document).ready(function(){

  $(".app .student-questions #hand-raised-question-alert").click(function() {
    $(this).hide();
  });

  var future = Math.round(new Date().getTime()/1000) + 6000;
  setInterval(function() {
    var s = getHoursMinuteFormat(future - Math.round(new Date().getTime()/1000)) + "s";
    $(".app .class-time-left h4.text").html(s);
  }, 1000);

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
