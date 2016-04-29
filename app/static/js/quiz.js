/* input is array of object arrays planets, people, and species 
   output is array of objects arrays questions, answers, and correct answers */
function generate_quiz(data)
{
	already_scored = false;
	questions = [];
	correct = [];
	all_answers = [];

	/* For generating questions */
	groups = ["the planet","","the species"];
	table_names=["planets","people","species"];

	/* For choosing answers */
	acceptable_keys=[["climate","population","terrain"],["birth_year","eye_color","hair_color","height","species"],["classification","homeworld","language"]];
	bad_answers=["unknown","n/a"];

	/* Generates data for single question */
	for(i = 0; i < 10; i++)
	{
		/* Gets random topic of random table to use for question */
		var question = {};
		var table_id = Math.floor(Math.random() * 3);
		var table = data[table_id][table_names[table_id]];
		var topic = acceptable_keys[table_id][Math.floor(Math.random() * acceptable_keys[table_id].length)];

		answers = [];
		n = 0;
		/* Gets an acceptable answer to use as the correct answer */
		while(n<1)
		{
			/* Gets random data from table and poic to use as answer */
			var correct_answer_id = Math.floor(Math.random() * table.length);
			var answer = table[correct_answer_id][topic];

			/* Checks to make sure that answer is not null, does not contain a bad answer, and is not part of a bad answer */
			if(answer!=null)
			{
    			for(ans in bad_answers)
    			{
    				if(answer.toLowerCase().indexOf(bad_answers[ans].toLowerCase())<0 && bad_answers[ans].toLowerCase().indexOf(answer.toLowerCase())<0)
    				{
    					answers.push(answer);
    					n++;
    					break;
    				}
    			}
			}

		}
		while( n<4 )
		{
			/* Gets random data from table and poic to use as answer */
			var answer = table[Math.floor(Math.random() * table.length)][topic];
			var good_answer = true;

			/* 
			 * Checks to make sure that answer is not null
			 * does not contain a previous answer
			 * is not part of a previous answer
			 * does not contain a bad answer
			 * is not part of a bad answer 
			 */
			if(answer!=null)
			{
				for(ans in answers)
    			{
    				if(answer.toLowerCase().indexOf(answers[ans].toLowerCase())>=0 || answers[ans].toLowerCase().indexOf(answer.toLowerCase())>=0)
    					good_answer = false;
    			}
    			for(ans in bad_answers)
    			{
    				if(answer.toLowerCase().indexOf(bad_answers[ans].toLowerCase())>=0 || bad_answers[ans].toLowerCase().indexOf(answer.toLowerCase())>=0)
    					good_answer = false;
    			}
    			if(good_answer == true)
    			{
					answers.push(answer);
					n++;
				}
			}
		}
		/* Shuffles answers to disperse correct randomly throughout wrong */
		shuffle(answers);

		/* Generates text of question */
		questions.push("What is the "+topic.replace('_', ' ')+" of "+groups[table_id]+" "+table[correct_answer_id]["name"]+"?");

		/* Pushes answers and correct answers onto arrays */
		all_answers.push(answers);
		correct.push(table[correct_answer_id][topic]);
	}
	return [questions,all_answers,correct];
}

/* Shuffles input array */
function shuffle(a)
{
    var j, x, i;
    for (i = a.length; i; i -= 1) {
        j = Math.floor(Math.random() * i);
        x = a[i - 1];
        a[i - 1] = a[j];
        a[j] = x;
    }
}

/* Computes the score and sets the html for the score */
function get_score()
{
	if(!already_scored)
	{
		var score = 0;

		/* Checks that the radion button label is queal to the correct value */
		for(i = 0; i < 10; i++)
		{
			if(document.querySelector('input[name = "question-'+i+'"]:checked')!=null && correct[i]==document.getElementById("for-"+document.querySelector('input[name = "question-'+i+'"]:checked').id).innerHTML)
			{
				score++;
			}
			else
			{
				document.getElementById("correct-"+i).innerHTML="Correct Answer: "+correct[i];
			}
		}

		document.getElementById("score").innerHTML="<h1>Score: "+score+"<h1>";
		already_scored = true;
	}
}
