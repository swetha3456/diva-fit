import torch
import nltk
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import AutoTokenizer, pipeline
from langchain import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
import sys


# create vector store and question-answering pipeline

# Load text file
loader = TextLoader("data.txt")
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings()
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(docs, embedding_model)
vector_store.save_local("faiss_index")


# Create a tokenizer object by loading the pretrained "Intel/dynamic_tinybert" tokenizer.
tokenizer = AutoTokenizer.from_pretrained("Intel/dynamic_tinybert")

# Create a question-answering model object by loading the pretrained "Intel/dynamic_tinybert" model.
model = AutoModelForQuestionAnswering.from_pretrained("Intel/dynamic_tinybert")

# Define a question-answering pipeline
question_answerer = pipeline(
    "question-answering", 
    model=model, 
    tokenizer=tokenizer
)

# Wrap the pipeline in a HuggingFacePipeline
llm = HuggingFacePipeline(
    pipeline=question_answerer,
    model_kwargs={"temperature": 0.7, "max_length": 512},
)

retriever = vector_store.as_retriever(search_kwargs={"k": 1})
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="refine", retriever=retriever, return_source_documents=False)

def err_remove(er):
    lin = "------------"
    er = str(er)
    start_index = er.find(lin) + len(lin)
    end_index = er.rfind(lin)
    Answer = er[start_index:end_index].strip()
    return Answer


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
    "period" : "It's important to listen to your body during your period. Light exercises like walking or gentle yoga can help alleviate discomfort. However, if you're feeling particularly fatigued, it's okay to take a break.",
    "pain": "It's important to be cautious whiel exercising. If facing any pain, consult a doctor before continuing any exercises."
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


def predict(input_text):
    print('here')
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
    
    try:
        result = qa.invoke({"query": "How do I get started with strength training?"})
        answer = result["result"]
    except:
        _,error,_ = sys.exc_info()
        answer = err_remove(error)


    keyword_op = ' '.join(exercise_advice[keyword] for keyword in keywords if keyword in exercise_advice)

    if answer is not None:
        return age + answer + ' ' + keyword_op
    else:
        return age + keyword_op
