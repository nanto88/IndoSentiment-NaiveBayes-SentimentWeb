// $(".setting").hide();
// $(".advanced").hide();
$(document).ready(function(){

    var d = new Date();
    d.setDate(d.getDate() - 6);

    $('input[name="daterange"]').daterangepicker({
      opens: 'left',
      autoUpdateInput: false,
      minDate: d.toLocaleDateString(),
      maxDate: new Date()
    }, function(start, end) {
          $('input[name="daterange"]').val(start.format('MM/DD/YYYY') + ' - ' + end.format('MM/DD/YYYY'));
        },
        function(start, end, label) {
          console.log("A new date selection was made: " + start.format('MM/DD/YYYY') + ' to ' + end.format('MM/DD/YYYY'));
        });


    $(".toggle").click(function(){
      $(".setting").fadeToggle('ease')

      // $(".text-muted").text(function(_,txt){
      //   var newtxt = "";
      //   if ( txt == "<i class='fa fa-caret-right'></i> Set Daterange") {
      //     newtxt = "<i class='fa fa-caret-right'></i> Set Pencarian Terbaru";
      //   }
      //   else {
      //     newtxt = "<i class='fa fa-caret-right'></i> Set Daterange"
      //   }
      //   return newtxt;
      // });
      // return false;

      $("i").toggleClass("fa-caret-right fa-caret-down")

    });
    $(".checkbox").change(function(){
      if(this.checked) {
        $('.date').fadeOut('ease');
        $('.date').val("");
      }  else if (this.checked == false) {
        $('.date').fadeIn('ease');
      }

    });

    $(".toggle2").click(function(){
      $(".advanced").fadeToggle("ease")
      $(".iconadv").toggleClass("fa-angle-double-right fa-angle-double-down")
    });






});
