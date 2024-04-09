def get_recommendation(phase, age_group, fitness_goal):
    if phase == 'mestrual':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                text = "Nutrition: Focus on balanced meals with lean proteins, whole grains, and plenty of fruits and vegetables to support weight management and provide essential nutrients. Exercise: Engage in moderate-intensity activities like brisk walking, cycling, or dancing to burn calories and improve mood. Hydration: Drink water and herbal teas to stay hydrated and reduce bloating."
            elif fitness_goal == "gain strength":
                text = "Nutrition: Consume adequate protein to support muscle repair and growth, along with complex carbohydrates for sustained energy. Exercise: Incorporate strength training exercises such as bodyweight squats, lunges, and push-ups to build muscle and improve overall strength. Rest: Ensure sufficient rest between workouts to allow muscles to recover and grow."
            elif fitness_goal == "gain weight":
                text = "Nutrition: Increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and healthy oils to promote weight gain in a healthy manner. Exercise: Focus on strength training exercises to build muscle mass, combined with compound movements like deadlifts and bench presses. Hydration: Drink fluids regularly to stay hydrated and support muscle function."
        elif age_group == "young adult":
            if fitness_goal == "lose weight":
                text = "Nutrition: Track calorie intake and focus on portion control, incorporating whole foods and limiting processed foods and added sugars. Exercise: Include a combination of cardiovascular exercises like running or HIIT workouts with strength training to maximize calorie burn and fat loss. Sleep: Prioritize quality sleep to support metabolism and overall well-being."
            elif fitness_goal == "gain strength":
                text = "Nutrition: Consume sufficient protein from sources like lean meats, dairy, and plant-based proteins to support muscle repair and growth. Exercise: Follow a structured strength training program focusing on compound exercises like squats, deadlifts, and bench presses, gradually increasing weights and intensity. Recovery: Allow adequate rest between workouts to prevent overtraining and promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                text = "Nutrition: Increase calorie intake with nutrient-dense foods like lean proteins, complex carbohydrates, and healthy fats, aiming for a slight caloric surplus to support weight gain. Exercise: Incorporate strength training exercises targeting all major muscle groups, progressively increasing weights and volume to stimulate muscle growth. Consistency: Maintain a consistent workout schedule and nutrition plan to support steady weight gain over time."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                text = "Nutrition: Focus on nutrient-rich, lower-calorie foods like fruits, vegetables, lean proteins, and whole grains to support weight loss and overall health. Exercise: Engage in low-impact activities such as walking, swimming, or cycling to burn calories without putting excess strain on joints. Portion Control: Practice mindful eating and portion control to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                text = "Nutrition: Prioritize protein intake to support muscle maintenance and repair, along with adequate hydration to support overall health and performance. Exercise: Incorporate strength training exercises using light weights or resistance bands to improve muscular strength and function, focusing on proper form and technique. Balance and Stability: Include exercises that improve balance and stability, such as yoga or tai chi, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                text = "Nutrition: Consume calorie-dense foods like nuts, nut butter, full-fat dairy, and lean proteins to increase calorie intake and support weight gain. Exercise: Engage in resistance training exercises using light weights or resistance bands to build muscle mass and strength, focusing on gradual progression and proper form. Appetite: Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain goals."
    elif phase == 'follicular':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the follicular phase, focus on balanced meals with lean proteins, whole grains, and plenty of fruits and vegetables to support weight management and provide essential nutrients. Exercise: Engage in moderate-intensity activities like brisk walking, cycling, or dancing to burn calories and improve mood. Hydration: Drink water and herbal teas to stay hydrated and reduce bloating."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the follicular phase, consume adequate protein to support muscle repair and growth, along with complex carbohydrates for sustained energy. Exercise: Incorporate strength training exercises such as bodyweight squats, lunges, and push-ups to build muscle and improve overall strength. Rest: Ensure sufficient rest between workouts to allow muscles to recover and grow."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the follicular phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and healthy oils to promote weight gain in a healthy manner. Exercise: Focus on strength training exercises to build muscle mass, combined with compound movements like deadlifts and bench presses. Hydration: Drink fluids regularly to stay hydrated and support muscle function."
        elif age_group == "young adult":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the follicular phase, track calorie intake and focus on portion control, incorporating whole foods and limiting processed foods and added sugars. Exercise: Include a combination of cardiovascular exercises like running or HIIT workouts with strength training to maximize calorie burn and fat loss. Sleep: Prioritize quality sleep to support metabolism and overall well-being."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the follicular phase, consume sufficient protein from sources like lean meats, dairy, and plant-based proteins to support muscle repair and growth. Exercise: Follow a structured strength training program focusing on compound exercises like squats, deadlifts, and bench presses, gradually increasing weights and intensity. Recovery: Allow adequate rest between workouts to prevent overtraining and promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the follicular phase, increase calorie intake with nutrient-dense foods like lean proteins, complex carbohydrates, and healthy fats, aiming for a slight caloric surplus to support weight gain. Exercise: Incorporate strength training exercises targeting all major muscle groups, progressively increasing weights and volume to stimulate muscle growth. Consistency: Maintain a consistent workout schedule and nutrition plan to support steady weight gain over time."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the follicular phase, focus on nutrient-rich, lower-calorie foods like fruits, vegetables, lean proteins, and whole grains to support weight loss and overall health. Exercise: Engage in low-impact activities such as walking, swimming, or cycling to burn calories without putting excess strain on joints. Portion Control: Practice mindful eating and portion control to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the follicular phase, prioritize protein intake to support muscle maintenance and repair, along with adequate hydration to support overall health and performance. Exercise: Incorporate strength training exercises using light weights or resistance bands to improve muscular strength and function, focusing on proper form and technique. Balance and Stability: Include exercises that improve balance and stability, such as yoga or tai chi, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the follicular phase, consume calorie-dense foods like nuts, nut butter, full-fat dairy, and lean proteins to increase calorie intake and support weight gain. Exercise: Engage in resistance training exercises using light weights or resistance bands to build muscle mass and strength, focusing on gradual progression and proper form. Appetite: Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain goals."
    elif phase == 'ovulation':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the ovulation phase, focus on consuming balanced meals rich in lean proteins, healthy fats, and fiber to support weight management and hormone balance. Exercise: Engage in a variety of physical activities such as cardio, strength training, and yoga to maintain overall fitness and energy levels. Hydration: Drink plenty of water and electrolyte-rich beverages to stay hydrated and support optimal bodily functions."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the ovulation phase, prioritize protein intake to support muscle repair and growth, and consume complex carbohydrates for sustained energy during workouts. Exercise: Incorporate compound exercises like squats, deadlifts, and bench presses into your strength training routine to maximize muscle activation and strength gains. Recovery: Ensure adequate rest and sleep to promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the ovulation phase, increase calorie intake with nutrient-dense foods like nuts, seeds, whole grains, and lean proteins to support weight gain goals. Exercise: Focus on progressive overload during strength training sessions by gradually increasing weights and/or repetitions to stimulate muscle growth. Hydration: Drink enough fluids to stay hydrated, especially if engaging in intense workouts to support muscle function and recovery."
        elif age_group == "young adult":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the ovulation phase, prioritize whole foods rich in vitamins, minerals, and antioxidants, and limit processed foods and added sugars to support weight loss efforts. Exercise: Incorporate high-intensity interval training (HIIT) or circuit training workouts to maximize calorie burn and boost metabolism. Recovery: Allow time for rest and recovery between workouts to prevent overtraining and support muscle repair."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the ovulation phase, aim for a balanced diet with adequate protein, carbohydrates, and healthy fats to fuel workouts and support muscle growth. Exercise: Incorporate a variety of resistance training exercises targeting different muscle groups to promote overall strength and muscular balance. Consistency: Stick to a regular workout schedule and progressively overload your muscles to continue seeing strength gains."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the ovulation phase, increase calorie intake with nutrient-dense foods like lean meats, dairy, whole grains, and healthy fats to support weight gain goals. Exercise: Focus on compound exercises that target multiple muscle groups, such as squats, deadlifts, and rows, and gradually increase weights and volume over time. Hydration: Drink plenty of fluids, including water and sports drinks, to stay hydrated and support muscle recovery."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the ovulation phase, emphasize whole, nutrient-dense foods like fruits, vegetables, lean proteins, and whole grains, and limit processed foods and sugary snacks to support weight loss and overall health. Exercise: Engage in low-impact activities like walking, swimming, or cycling to burn calories and improve cardiovascular health. Mindful Eating: Pay attention to hunger and fullness cues to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the ovulation phase, focus on consuming adequate protein to support muscle repair and maintenance, and include healthy fats and carbohydrates for sustained energy. Exercise: Incorporate resistance training exercises using bodyweight, resistance bands, or light weights to improve muscle strength and endurance. Balance and Stability: Include exercises that improve balance and coordination, such as tai chi or yoga, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the ovulation phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and lean proteins to support weight gain goals. Exercise: Engage in strength training exercises using resistance bands or light weights to build muscle mass and improve overall strength. Appetite: Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain and muscle growth."
    elif phase == 'luteal':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the luteal phase, focus on consuming a balanced diet rich in fruits, vegetables, whole grains, and lean proteins to support weight loss goals and manage cravings. Exercise: Engage in moderate-intensity activities like brisk walking, swimming, or cycling to burn calories and reduce stress levels. Stress Management: Practice relaxation techniques such as deep breathing, meditation, or yoga to manage stress and emotional eating."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the luteal phase, prioritize protein-rich foods like eggs, poultry, fish, and legumes to support muscle repair and growth. Exercise: Incorporate strength training exercises using resistance bands or free weights to maintain muscle mass and improve overall strength. Recovery: Allow for adequate rest and recovery between workouts to prevent overtraining and promote muscle repair."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the luteal phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and whole milk to support weight gain goals. Exercise: Focus on compound exercises that target multiple muscle groups, such as squats, deadlifts, and bench presses, and gradually increase weights and volume to promote muscle growth. Hydration: Drink plenty of fluids to stay hydrated and support muscle recovery."
        elif age_group == "young adult":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the luteal phase, emphasize portion control and choose nutrient-dense foods like fruits, vegetables, whole grains, and lean proteins to support weight loss efforts. Exercise: Incorporate a mix of cardio and strength training exercises to maximize calorie burn and preserve lean muscle mass. Stress Management: Practice stress-reducing activities like yoga, meditation, or spending time outdoors to manage stress and prevent emotional eating."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the luteal phase, aim for a balanced diet with adequate protein, carbohydrates, and healthy fats to fuel workouts and support muscle repair and growth. Exercise: Continue with your regular strength training routine, focusing on progressive overload and incorporating a variety of exercises to target different muscle groups. Recovery: Prioritize rest and recovery to allow your muscles to repair and grow stronger."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the luteal phase, increase calorie intake with nutrient-dense foods like lean meats, dairy, whole grains, and healthy fats to support weight gain goals. Exercise: Incorporate compound exercises that target multiple muscle groups, such as squats, deadlifts, and rows, and gradually increase weights and volume over time. Hydration: Drink plenty of fluids, including water and sports drinks, to stay hydrated and support muscle recovery."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                text = "Nutrition: During the luteal phase, focus on portion control and choose nutrient-rich foods like fruits, vegetables, whole grains, and lean proteins to support weight loss goals. Exercise: Engage in low-impact activities like walking, swimming, or yoga to burn calories and improve cardiovascular health. Stress Management: Practice stress-relieving activities such as meditation, deep breathing, or spending time with loved ones to manage stress and prevent emotional eating."
            elif fitness_goal == "gain strength":
                text = "Nutrition: During the luteal phase, ensure adequate protein intake to support muscle repair and growth, and include healthy fats and carbohydrates for sustained energy. Exercise: Incorporate resistance training exercises using bodyweight, resistance bands, or light weights to improve muscle strength and endurance. Recovery: Allow for sufficient rest and recovery between workouts to prevent overtraining and promote muscle repair and growth."
            elif fitness_goal == "gain weight":
                text = "Nutrition: During the luteal phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and lean proteins to support weight gain goals. Exercise: Engage in strength training exercises using resistance bands or light weights to build muscle mass and improve overall strength. Appetite: Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain and muscle growth."
    return text

# Example usage:
age_group = "teen"
fitness_goal = "lose weight"
phase = 'menstrual'
recommendation = get_recommendation(phase, age_group, fitness_goal)
print(recommendation)
