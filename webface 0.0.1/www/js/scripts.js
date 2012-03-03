
	function sendCommand(){

		var command = $('#command').val();

		if(command == ''){
			$('#result').html("Please enter a command.");
			exit;
		}

		$.post("", {command: command}, function(data) {

			$('#result').html(data);
			
		});
		
	}
	