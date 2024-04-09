from transformers import BertTokenizer, BertForQuestionAnswering
import torch
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')

# # Load the BERT model and tokenizer
# tokenizer = BertTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
# model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')


# model_load_path = 'model.pt'

# # Load the model
# model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')  # Instantiate your model class
# model.load_state_dict(torch.load(model_load_path))

# # Ensure the model is in evaluation mode
# model.eval()

data = [
                 ("I want to improve my strength. What exercises do you recommend?", "Strength training exercises like squats, deadlifts, and bench presses can help you build muscle."),
                 ("I feel very tired during my period. Should I still exercise?", "It's important to listen to your body during your period. Light exercises like walking or gentle yoga can help alleviate discomfort. However, if you're feeling particularly fatigued, it's okay to take a break."),
                 ("How can I improve my flexibility?", "Incorporating stretching exercises like yoga or Pilates into your routine can help improve flexibility."),
                ("I'm feeling overwhelmed by all the conflicting information about exercise. How can I determine what's best for me?", "It's common to feel overwhelmed by the abundance of information available about exercise and fitness. Start by focusing on the basics: regular physical activity, a balanced diet, and listening to your body's signals. Experiment with different types of exercises and routines to see what works best for you, and don't hesitate to seek guidance from a qualified fitness professional if you need help."),
        ("I'm feeling stressed. Will exercise help?", "Exercise is a great way to reduce stress and improve mood. Physical activity releases endorphins, which are chemicals in the brain that act as natural painkillers and mood elevators. Try incorporating activities like walking, jogging, or yoga into your routine to help manage stress."),
        ("What are some exercises I can do to improve my posture?", "Exercises like rows, shoulder blade squeezes, and core strengthening exercises can help improve posture. Additionally, practicing good posture throughout the day is important."),
        ("I have trouble staying motivated to exercise regularly. Any tips?", "Setting specific, achievable goals, finding a workout buddy for accountability, and varying your routine with different types of exercises can help keep you motivated. Remember to focus on how exercise makes you feel, rather than just the end results."),
                   ("I'm not seeing the results I want from my workouts. What am I doing wrong?", "Several factors could be contributing to a lack of results, including not exercising with enough intensity or frequency, poor nutrition, inadequate recovery time, or unrealistic expectations. Consider evaluating your workout routine, nutrition habits, and lifestyle factors to identify areas for improvement."),
                 ("What should I eat before and after a workout?", "Before a workout, it's important to fuel your body with a combination of carbohydrates and protein for energy and muscle repair. Consider options like a banana with peanut butter, Greek yogurt with fruit, or a turkey sandwich on whole-grain bread. After a workout, aim to consume a balanced meal or snack containing protein and carbohydrates to replenish energy stores and support muscle recovery."),
                 ("I'm traveling and don't have access to a gym. What are some exercises I can do without equipment?", "Bodyweight exercises like push-ups, squats, lunges, and planks are great options for working out while traveling. You can also incorporate resistance bands or use household items like water bottles or backpacks as makeshift weights."),
                    ("I'm pregnant. What exercises are safe for me to do?", "Congratulations! Low-impact exercises like swimming, walking, and prenatal yoga are generally safe during pregnancy. It's best to consult with your healthcare provider before starting any new exercise routine."),
                 ("I have a knee injury. What exercises can I do to strengthen my knee?", "Exercises that focus on strengthening the muscles around the knee, such as leg lifts and hamstring curls, can help improve knee stability. It's important to avoid exercises that cause pain or discomfort."),
                 ("I'm trying to lose weight. What types of exercises are best for burning calories?", "Cardiovascular exercises like running, cycling, and HIIT workouts are effective for burning calories. Additionally, incorporating strength training exercises can help increase muscle mass and boost metabolism."),
    ("I'm in my 60s and want to stay active. What exercises are suitable for seniors?", 
     "Seniors can benefit from activities like walking, water aerobics, gentle yoga, tai chi, and resistance training using light weights or resistance bands to maintain mobility, strength, and balance."),
     
    ("What exercises can teenagers do to stay active?", 
     "Teenagers can participate in team sports, individual sports, strength training, yoga, and other activities to stay active and healthy during their adolescent years."),
    
    ("I'm in my 20s and want to improve my fitness. What exercises do you recommend?", 
     "In your 20s, you can focus on a variety of exercises including strength training, cardio (such as running, cycling, or swimming), HIIT workouts, and flexibility training to improve overall fitness.")
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

exercise_advice = {
    "aerobics": "Mix up your aerobic workouts with different activities to prevent boredom.",
    "weightlifting": "Start with lighter weights and focus on proper form before increasing intensity.",
    "cardio": "Incorporate both steady-state cardio and high-intensity intervals for optimal heart health.",
    "running": "Listen to your body and gradually increase mileage to prevent injury.",
    "walking": "Take advantage of daily walks as a simple yet effective form of exercise.",
    "jogging": "Warm up properly before jogging and cool down afterward to prevent muscle strain.",
    "cycling": "Explore new cycling routes to keep your rides exciting and challenging.",
    "swimming": "Use swimming as a low-impact yet effective full-body workout option.",
    "yoga": "Focus on proper breathing and mindfulness to enhance the benefits of yoga practice.",
    "pilates": "Engage your core muscles throughout Pilates exercises for maximum effectiveness.",
    "stretching": "Incorporate stretching into your routine to improve flexibility and prevent injury.",
    "strength": "Progressively overload your muscles by gradually increasing resistance or repetitions.",
    "interval": "Alternate between periods of high-intensity exercise and recovery for maximum results.",
    "HIIT": "Challenge yourself with high-intensity interval training for efficient calorie burning.",
    "calisthenics": "Master the basics of bodyweight exercises before advancing to more complex movements.",
    "crossfit": "Embrace the community aspect of CrossFit while focusing on proper form and safety.",
    "circuit": "Design circuit workouts that target different muscle groups for a full-body burn.",
    "dancing": "Express yourself through dance while getting a great cardiovascular workout.",
    "zumba": "Join a Zumba class for a fun and energetic way to improve cardiovascular fitness.",
    "kickboxing": "Channel your inner fighter and unleash stress with kickboxing workouts.",
    "piloxing": "Combine Pilates, boxing, and dance for a dynamic and challenging workout.",
    "barre": "Focus on small, controlled movements to sculpt and tone muscles in a barre class.",
    "hiking": "Enjoy the great outdoors and reap the physical and mental benefits of hiking.",
    "climbing": "Challenge yourself both physically and mentally with indoor or outdoor climbing.",
    "rowing": "Master proper rowing technique to maximize the cardiovascular and strength benefits.",
    "jumping": "Incorporate plyometric exercises like jumping to improve power and explosiveness.",
    "squats": "Maintain proper form and engage your core muscles during squat exercises.",
    "push-ups": "Start with modified push-ups and progress to full push-ups for upper body strength.",
    "pull-ups": "Use bands or assisted machines to build up to unassisted pull-ups gradually.",
    "planks": "Engage your core muscles and keep your body in a straight line during plank exercises.",
    "lunges": "Focus on proper alignment and avoid letting your knees go past your toes during lunges.",
    "burpees": "Push yourself with this full-body exercise that combines strength and cardio.",
    "deadlifts": "Master proper deadlift form to safely strengthen your posterior chain muscles.",
    "bench": "Start with light weights and gradually increase as you build strength on the bench press.",
    "crunches": "Focus on lifting your shoulder blades off the ground using your abdominal muscles.",
    "sit-ups": "Engage your core muscles and avoid pulling on your neck during sit-up exercises.",
    "bicycle": "Alternate between slow and controlled movements to engage your core during bicycle crunches.",
    "leg": "Focus on engaging your glutes and hamstrings during leg exercises like squats and lunges.",
    "Russian": "Keep your core engaged and rotate from your torso during Russian twists.",
    "mountain": "Maintain a strong plank position while bringing your knees towards your chest during mountain climbers.",
    "high": "Focus on driving your knees up towards your chest during high knees for maximum impact.",
    "squat": "Keep your chest up and weight in your heels as you lower into a squat position.",
    "jumping": "Focus on landing softly with bent knees to reduce impact during jumping exercises.",
    "box": "Focus on explosiveness and control as you jump onto and off of a box.",
    "kettlebell": "Master proper kettlebell swinging technique before increasing weight or intensity.",
    "medicine": "Incorporate medicine ball exercises to improve strength, power, and coordination.",
    "resistance": "Use resistance bands to add variety and challenge to your workouts.",
    "dumbbell": "Start with lighter weights and focus on proper form before increasing resistance.",
    "barbell": "Engage your core muscles and maintain proper form during barbell exercises.",
    "bodyweight": "Master bodyweight exercises like push-ups and squats before adding external resistance.",
    "plyometrics": "Focus on explosive movements to improve power and athleticism with plyometric exercises.",
    "functional": "Incorporate functional exercises that mimic real-life movements for improved daily function.",
    "core": "Strengthen your core muscles to improve stability and prevent injury in other activities.",
    "balance": "Incorporate balance exercises like single-leg stands to improve stability and prevent falls.",
    "flexibility": "Incorporate dynamic and static stretches to improve flexibility and prevent injury.",
    "mobility": "Focus on joint mobility exercises to improve range of motion and prevent stiffness.",
    "cool": "Gradually lower your heart rate and stretch to prevent muscle soreness and promote recovery.",
    "warm": "Increase blood flow to muscles and prepare your body for exercise with a dynamic warm-up.",
    "stretches": "Incorporate a variety of stretches targeting different muscle groups for improved flexibility.",
    "exercise": "Consistency is key; make it a habit to move your body regularly.",
    "exercises": "Consistency is key; make it a habit to move your body regularly.",
    "exercising": "Consistency is key; make it a habit to move your body regularly.", 
    "workout": "Challenge yourself with different workouts to keep things interesting.",
    "activity": "Find activities you enjoy to make exercise feel like fun, not work.",
    "fitness": "Focus on progress, not perfection, and celebrate your achievements.",
    "training": "Set specific goals for your training sessions to stay motivated and track progress.",
    "period" : "It's important to listen to your body during your period. Light exercises like walking or gentle yoga can help alleviate discomfort. However, if you're feeling particularly fatigued, it's okay to take a break."
}

def get_keywords(input_text):

    # Tokenize the text
    tokens = nltk.word_tokenize(input_text)

    # Create a list of stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))

    # Remove stop words from the tokens
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Create a list of keywords
    keywords = []
    for token in filtered_tokens:
        if token.isalpha() and len(token) > 2:
            keywords.append(token)

    return keywords

def age_related(age):
    if age < 12:
        return "Children should engage in a variety of physical activities including running, jumping, climbing, biking, and playing sports to develop motor skills, strength, and coordination."
    elif age >= 12 and age < 19:
        return "Teenagers can participate in team sports, individual sports, strength training, yoga, and other activities to stay active and healthy during their adolescent years."
    elif age >= 19 and age < 30:
        return "In your 20s, you can focus on a variety of exercises including strength training, cardio (such as running, cycling, or swimming), HIIT workouts, and flexibility training to improve overall fitness."
    elif age >= 30 and age < 40:
        return "In your 30s, prioritizing regular physical activity such as brisk walking, jogging, dancing, or group fitness classes can help boost energy levels and improve mood."
    elif age >= 40 and age < 50:
        return "In your 40s, incorporating a mix of strength training, cardiovascular exercise, yoga, and flexibility exercises can help combat the effects of aging and maintain overall health."
    elif age >= 50 and age < 60:
        return "Low-impact exercises like swimming, cycling, walking, tai chi, and yoga are gentle on the joints and can help relieve joint pain and stiffness."
    elif age >= 60 and age < 70:
        return "Seniors can benefit from activities like walking, water aerobics, gentle yoga, tai chi, and resistance training using light weights or resistance bands to maintain mobility, strength, and balance."
    elif age >= 70 and age < 80:
        return "For seniors with mobility issues, chair exercises, gentle stretching, seated yoga, and aquatic therapy can provide safe and effective ways to stay active and maintain functional mobility."
    elif age >= 80 and age < 90:
        return "In your 80s, focusing on exercises that improve balance, strength, and flexibility, such as seated exercises, balance drills, and light resistance training, can help maintain independence and reduce the risk of falls."
    elif age >= 90:
        return "For individuals in their 90s, gentle movements like seated stretches, chair yoga, and breathing exercises can promote circulation, maintain range of motion, and contribute to overall well-being."


def predict(input_text, model):
    flag = False

    for x in input_text.split():
        if x.isdigit() or x.strip('s').isdigit() or x.strip('.').isdigit() or x.strip(',').isdigit():
            x = x.strip('s')
            x = x.strip(',')
            x = x.strip('.')
            age = age_related(int(x))
        else:
            age = ''
    keywords = get_keywords(input_text)
    for word in keywords:
        if word in exercise_advice:
            flag = True
            break
    if flag == False and age == '':
        return "Please try an exercise related question."
    
    ans = _predict(input_text, model)

    keyword_op = ' '.join(exercise_advice[keyword] for keyword in keywords if keyword in exercise_advice)

    if ans is not None:
        return age + ans + ' ' + keyword_op
    else:
        return age + keyword_op

def _predict(input_text, model):
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

    if prediction == 0:
        return None

    try:
        return answers[prediction - 1]
    except:
        return None
    
    