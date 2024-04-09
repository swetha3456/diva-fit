from transformers import BertTokenizer, BertForQuestionAnswering
import torch

# Load the BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')


model_load_path = 'model.pt'

# Load the model
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')  # Instantiate your model class
model.load_state_dict(torch.load(model_load_path))

# Ensure the model is in evaluation mode
model.eval()

data = [
                 ("I want to improve my strength. What exercises do you recommend?", "Strength training exercises like squats, deadlifts, and bench presses can help you build muscle. Do you have any equipment available or prefer bodyweight exercises?"),
                 ("I feel very tired during my period. Should I still exercise?", "It's important to listen to your body during your period. Light exercises like walking or gentle yoga can help alleviate discomfort. However, if you're feeling particularly fatigued, it's okay to take a break."),
                 ("How can I improve my flexibility?", "Incorporating stretching exercises like yoga or Pilates into your routine can help improve flexibility. Would you like some specific stretches to try?"),
                ("I'm feeling overwhelmed by all the conflicting information about exercise. How can I determine what's best for me?", "It's common to feel overwhelmed by the abundance of information available about exercise and fitness. Start by focusing on the basics: regular physical activity, a balanced diet, and listening to your body's signals. Experiment with different types of exercises and routines to see what works best for you, and don't hesitate to seek guidance from a qualified fitness professional if you need help."),
        ("I'm feeling stressed. Will exercise help?", "Exercise is a great way to reduce stress and improve mood. Physical activity releases endorphins, which are chemicals in the brain that act as natural painkillers and mood elevators. Try incorporating activities like walking, jogging, or yoga into your routine to help manage stress."),
        ("What are some exercises I can do to improve my posture?", "Exercises like rows, shoulder blade squeezes, and core strengthening exercises can help improve posture. Additionally, practicing good posture throughout the day is important."),
        ("I have trouble staying motivated to exercise regularly. Any tips?", "Setting specific, achievable goals, finding a workout buddy for accountability, and varying your routine with different types of exercises can help keep you motivated. Remember to focus on how exercise makes you feel, rather than just the end results."),
                   ("I'm not seeing the results I want from my workouts. What am I doing wrong?", "Several factors could be contributing to a lack of results, including not exercising with enough intensity or frequency, poor nutrition, inadequate recovery time, or unrealistic expectations. Consider evaluating your workout routine, nutrition habits, and lifestyle factors to identify areas for improvement."),
                 ("What should I eat before and after a workout?", "Before a workout, it's important to fuel your body with a combination of carbohydrates and protein for energy and muscle repair. Consider options like a banana with peanut butter, Greek yogurt with fruit, or a turkey sandwich on whole-grain bread. After a workout, aim to consume a balanced meal or snack containing protein and carbohydrates to replenish energy stores and support muscle recovery."),
                 ("I'm traveling and don't have access to a gym. What are some exercises I can do without equipment?", "Bodyweight exercises like push-ups, squats, lunges, and planks are great options for working out while traveling. You can also incorporate resistance bands or use household items like water bottles or backpacks as makeshift weights."),
                    ("I'm pregnant. What exercises are safe for me to do?", "Congratulations! Low-impact exercises like swimming, walking, and prenatal yoga are generally safe during pregnancy. It's best to consult with your healthcare provider before starting any new exercise routine."),
                 ("I have a knee injury. What exercises can I do to strengthen my knee?", "Exercises that focus on strengthening the muscles around the knee, such as leg lifts and hamstring curls, can help improve knee stability. It's important to avoid exercises that cause pain or discomfort. Have you consulted with a physical therapist for personalized recommendations?"),
                 ("I'm trying to lose weight. What types of exercises are best for burning calories?", "Cardiovascular exercises like running, cycling, and HIIT workouts are effective for burning calories. Additionally, incorporating strength training exercises can help increase muscle mass and boost metabolism.")
]

questions = [item[0] for item in data]
answers = [item[1] for item in data]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

# Convert the data to input format for BERT
question_input_ids = []
question_attention_masks = []
for i in range(len(questions)):
    # Tokenize the question
    question_tokens = tokenizer.tokenize(questions[i])
    
    max_length = 512
    # Pad the input tokens
    question_tokens = question_tokens + [tokenizer.pad_token] * (max_length - len(question_tokens))

    # Create the input ids for the BERT model
    question_input_ids.append(tokenizer.convert_tokens_to_ids(question_tokens))

    # Create the attention masks for the input tokens
    question_attention_masks.append([1 if token != tokenizer.pad_token else 0 for token in question_tokens])

answer_input_ids = []
answer_attention_masks = []
for i in range(len(answers)):
    # Tokenize the answer
    answer_tokens = tokenizer.tokenize(answers[i])

    # Pad the input tokens
    answer_tokens = answer_tokens + [tokenizer.pad_token] * (max_length - len(answer_tokens))

    # Create the input ids for the BERT model
    answer_input_ids.append(tokenizer.convert_tokens_to_ids(answer_tokens))

    # Create the attention masks for the input tokens
    answer_attention_masks.append([1 if token != tokenizer.pad_token else 0 for token in answer_tokens])

# Concatenate the question and answer input lists
input_ids = question_input_ids + answer_input_ids
attention_masks = question_attention_masks + answer_attention_masks

# Convert the input ids and attention masks to tensors
input_ids = torch.tensor(input_ids).to(device)
attention_masks = torch.tensor(attention_masks).to(device)



def predict(input_text):
        # Define the input

    # Tokenize the input
    input_tokens = tokenizer.tokenize(input_text)

    # Pad the input tokens
    input_tokens = input_tokens + [tokenizer.pad_token] * (max_length - len(input_tokens))

    # Convert the input tokens to input ids
    input_ids = tokenizer.convert_tokens_to_ids(input_tokens)

    # Create the attention mask for the input
    attention_mask = [1 if token != tokenizer.pad_token else 0 for token in input_tokens]

    # Convert the input ids and attention mask to tensors
    input_ids = torch.tensor(input_ids).unsqueeze(0).to(device)
    attention_mask = torch.tensor(attention_mask).unsqueeze(0).to(device)

    # Get the model output
    output = model(input_ids, attention_mask=attention_mask)

    # Get the predicted label
    prediction = output[0].argmax(dim=1).item()

    # Print the output
    if prediction == 0:
        print("Question: {}".format(input_text))
    else:
        print("Answer: {}".format(answers[prediction - 1]))

predict(input_text = "What are some exercises I can do to improve my posture?")