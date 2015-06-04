$(document).ready(function() {
	$('table.display').dataTable();
	$('.barcode').each(function( index ) {
		var barcode = "";
		barcode = $(this).text();
		console.log(barcode);
		$( this ).barcode(barcode, "code128", {barHeight:20, fontSize:14});
	})
	
});