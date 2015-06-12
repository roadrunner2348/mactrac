$(document).ready(function() {
	$('table.display').dataTable({
		responsive: true
	});
	$('.barcode').each(function( index ) {
		var barcode = "";
		barcode = $(this).text();
		console.log(barcode);
		$( this ).barcode(barcode, "code128", {barHeight:20, fontSize:14});
	})
	$('select.chosen').chosen({disable_search_threshold: 10, width: "100%", search_contains: true});

	$('#form-submit').click(function() {
		$('form').submit();
	});
});