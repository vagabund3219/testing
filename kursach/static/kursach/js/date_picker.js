
if (/Mobi/.test(navigator.userAgent)) {
  // if mobile device, use native pickers
  $(".date input").attr("type", "date");
} else {
  // if desktop device, use DateTimePicker
  $("#datepicker").datepicker({
    useCurrent: false,
    // format: "DD-MMM-YYYY",
    format: "yy-mm-dd",
    altFormat: "yy-mm-dd",
    showTodayButton: true,
    icons: {
      next: "fa fa-chevron-right",
      previous: "fa fa-chevron-left",
      today: 'todayText',
    }
  });

}
