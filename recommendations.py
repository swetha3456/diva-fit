def get_recommendation(phase, age_group, fitness_goal):
    if fitness_goal not in ["lose weight", "gain weight", "gain strength"]:
        subhead1 = "Balance and Coordination"
        text1 = "Activities like tai chi, yoga, or balance exercises can improve balance and coordination, reducing the risk of falls and promoting overall stability."
        subhead2 = "Flexibility"
        text2 = "Regular stretching can improve flexibility and range of motion, making daily activities easier and reducing pain. Focus on gentle stretches that target major muscle groups."
        subhead3 = "Low-Impact Strength Training"
        text3 = "Building strength helps maintain bone density and muscle mass, which are important for overall health and function. Use bodyweight exercises, resistance bands, or light weights to strengthen major muscle groups."
    
    elif phase == 'menstrual':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Focus on balanced meals with lean proteins, whole grains, and plenty of fruits and vegetables to support weight management and provide essential nutrients."
                subhead2 = "Exercise"
                text2 = "Engage in moderate-intensity activities like brisk walking, cycling, or dancing to burn calories and improve mood."
                subhead3 = "Hydration"
                text3 = "Drink water and herbal teas to stay hydrated and reduce bloating."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "Consume adequate protein to support muscle repair and growth, along with complex carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate strength training exercises such as bodyweight squats, lunges, and push-ups to build muscle and improve overall strength."
                subhead3 = "Rest"
                text3 = "Ensure sufficient rest between workouts to allow muscles to recover and grow."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "Increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and healthy oils to promote weight gain in a healthy manner."
                subhead2 = "Exercise"
                text2 = "Focus on strength training exercises to build muscle mass, combined with compound movements like deadlifts and bench presses."
                subhead3 = "Hydration"
                text3 = "Drink fluids regularly to stay hydrated and support muscle function."
        elif age_group == "adult":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Track calorie intake and focus on portion control, incorporating whole foods and limiting processed foods and added sugars."
                subhead2 = "Exercise"
                text2 = "Include a combination of cardiovascular exercises like running or HIIT workouts with strength training to maximize calorie burn and fat loss."
                subhead3 = "Sleep"
                text3 = "Prioritize quality sleep to support metabolism and overall well-being."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "Consume sufficient protein from sources like lean meats, dairy, and plant-based proteins to support muscle repair and growth."
                subhead2 = "Exercise"
                text2 = "Follow a structured strength training program focusing on compound exercises like squats, deadlifts, and bench presses, gradually increasing weights and intensity."
                subhead3 = "Recovery"
                text3 = "Allow adequate rest between workouts to prevent overtraining and promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "Increase calorie intake with nutrient-dense foods like lean proteins, complex carbohydrates, and healthy fats, aiming for a slight caloric surplus to support weight gain."
                subhead2 = "Exercise"
                text2 = "Incorporate strength training exercises targeting all major muscle groups, progressively increasing weights and volume to stimulate muscle growth."
                subhead3 = "Consistency"
                text3 = "Maintain a consistent workout schedule and nutrition plan to support steady weight gain over time."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Focus on nutrient-rich, lower-calorie foods like fruits, vegetables, lean proteins, and whole grains to support weight loss and overall health."
                subhead2 = "Exercise"
                text2 = "Engage in low-impact activities such as walking, swimming, or cycling to burn calories without putting excess strain on joints."
                subhead3 = "Portion Control"
                text3 = "Practice mindful eating and portion control to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "Prioritize protein intake from sources like lean meats, fish, and dairy to support muscle maintenance and repair. Consume moderate amounts of complex carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate low-impact strength training exercises using light weights or resistance bands, focusing on proper form and technique. Gradually increase weight or resistance as tolerated."
                subhead3 = "Balance and Stability"
                text3 = "Include exercises that improve balance and stability, such as yoga or tai chi, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "Increase calorie intake with nutrient-dense foods like nuts, nut butter, full-fat dairy, and lean proteins to support weight gain. Consider adding healthy fats like avocado and olive oil. Ensure adequate hydration to support overall health and performance."
                subhead2 = "Exercise"
                text2 = "Focus on low-impact resistance training exercises using light weights or resistance bands, targeting all major muscle groups. Gradually increase weight or resistance and exercise volume over time."
                subhead3 = "Appetite"
                text3 = "Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain goals."
    
    elif phase == 'follicular':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Focus on balanced meals with lean proteins, whole grains, and plenty of fruits and vegetables to support weight management and provide essential nutrients."
                subhead2 = "Exercise"
                text2 = "Engage in moderate-intensity activities like brisk walking, cycling, or dancing to burn calories and improve mood."
                subhead3 = "Hydration"
                text3 = "Drink water and herbal teas to stay hydrated and reduce bloating."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "Consume adequate protein to support muscle repair and growth, along with complex carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate strength training exercises such as bodyweight squats, lunges, and push-ups to build muscle and improve overall strength."
                subhead3 = "Rest"
                text3 = "Ensure sufficient rest between workouts to allow muscles to recover and grow."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "Increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and healthy oils to promote weight gain in a healthy manner."
                subhead2 = "Exercise"
                text2 = "Focus on strength training exercises to build muscle mass, combined with compound movements like deadlifts and bench presses."
                subhead3 = "Hydration"
                text3 = "Drink fluids regularly to stay hydrated and support muscle function."
        elif age_group == "adult":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Track calorie intake and focus on portion control, incorporating whole foods and limiting processed foods and added sugars."
                subhead2 = "Exercise"
                text2 = "Include a combination of cardiovascular exercises like running or HIIT workouts with strength training to maximize calorie burn and fat loss."
                subhead3 = "Sleep"
                text3 = "Prioritize quality sleep to support metabolism and overall well-being."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "Consume sufficient protein from sources like lean meats, dairy, and plant-based proteins to support muscle repair and growth."
                subhead2 = "Exercise"
                text2 = "Follow a structured strength training program focusing on compound exercises like squats, deadlifts, and bench presses, gradually increasing weights and intensity."
                subhead3 = "Recovery"
                text3 = "Allow adequate rest between workouts to prevent overtraining and promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "Increase calorie intake with nutrient-dense foods like lean proteins, complex carbohydrates, and healthy fats, aiming for a slight caloric surplus to support weight gain."
                subhead2 = "Exercise"
                text2 = "Incorporate strength training exercises targeting all major muscle groups, progressively increasing weights and volume to stimulate muscle growth."
                subhead3 = "Consistency"
                text3 = "Maintain a consistent workout schedule and nutrition plan to support steady weight gain over time."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "Focus on nutrient-rich, lower-calorie foods like fruits, vegetables, lean proteins, and whole grains to support weight loss and overall health."
                subhead2 = "Exercise"
                text2 = "Engage in low-impact activities such as walking, swimming, or cycling to burn calories without putting excess strain on joints."
                subhead3 = "Portion Control"
                text3 = "Practice mindful eating and portion control to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the follicular phase, prioritize protein intake from sources like lean meats, fish, and dairy to support muscle maintenance and repair. Consume moderate amounts of complex carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate low-impact strength training exercises using light weights or resistance bands, focusing on proper form and technique. Gradually increase weight or resistance as tolerated."
                subhead3 = "Balance and Stability"
                text3 = "Include exercises that improve balance and stability, such as yoga or tai chi, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the follicular phase, increase calorie intake with nutrient-dense foods like nuts, nut butter, full-fat dairy, and lean proteins to support weight gain. Consider adding healthy fats like avocado and olive oil. Ensure adequate hydration to support overall health and performance."
                subhead2 = "Exercise"
                text2 = "Focus on low-impact resistance training exercises using light weights or resistance bands, targeting all major muscle groups. Gradually increase weight or resistance and exercise volume over time."
                subhead3 = "Appetite"
                text3 = "Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain goals."
    
    elif phase == 'ovulation':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, focus on consuming balanced meals rich in lean proteins, healthy fats, and fiber to support weight management and hormone balance."
                subhead2 = "Exercise"
                text2 = "Engage in a variety of physical activities such as cardio, strength training, and yoga to maintain overall fitness and energy levels."
                subhead3 = "Hydration"
                text3 = "Drink plenty of water and electrolyte-rich beverages to stay hydrated and support optimal bodily functions."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, prioritize protein intake to support muscle repair and growth, and consume complex carbohydrates for sustained energy during workouts."
                subhead2 = "Exercise"
                text2 = "Incorporate compound exercises like squats, deadlifts, and bench presses into your strength training routine to maximize muscle activation and strength gains."
                subhead3 = "Recovery"
                text3 = "Ensure adequate rest and sleep to promote muscle recovery and growth."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, increase calorie intake with nutrient-dense foods like nuts, seeds, whole grains, and lean proteins to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Focus on progressive overload during strength training sessions by gradually increasing weights and/or repetitions to stimulate muscle growth."
                subhead3 = "Hydration"
                text3 = "Drink enough fluids to stay hydrated, especially if engaging in intense workouts to support muscle function and recovery."
        elif age_group == "adult":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, prioritize whole foods rich in vitamins, minerals, and antioxidants, and limit processed foods and added sugars to support weight loss efforts."
                subhead2 = "Exercise"
                text2 = "Incorporate high-intensity interval training (HIIT) or circuit training workouts to maximize calorie burn and boost metabolism."
                subhead3 = "Recovery"
                text3 = "Allow time for rest and recovery between workouts to prevent overtraining and support muscle repair."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, aim for a balanced diet with adequate protein, carbohydrates, and healthy fats to fuel workouts and support muscle growth."
                subhead2 = "Exercise"
                text2 = "Incorporate a variety of resistance training exercises targeting different muscle groups to promote overall strength and muscular balance."
                subhead3 = "Consistency"
                text3 = "Stick to a regular workout schedule and progressively overload your muscles to continue seeing strength gains."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, increase calorie intake with nutrient-dense foods like lean meats, dairy, whole grains, and healthy fats to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Focus on compound exercises that target multiple muscle groups, such as squats, deadlifts, and rows, and gradually increase weights and volume over time."
                subhead3 = "Hydration"
                text3 = "Drink plenty of fluids, including water and sports drinks, to stay hydrated and support muscle recovery."
        elif age_group == "old":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, emphasize whole, nutrient-dense foods like fruits, vegetables, lean proteins, and whole grains, and limit processed foods and sugary snacks to support weight loss and overall health."
                subhead2 = "Exercise"
                text2 = "Engage in low-impact activities like walking, swimming, or cycling to burn calories and improve cardiovascular health."
                subhead3 = "Mindful Eating"
                text3 = "Pay attention to hunger and fullness cues to avoid overeating and support weight loss goals."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, focus on consuming adequate protein to support muscle repair and maintenance, and include healthy fats and carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate resistance training exercises using bodyweight, resistance bands, or light weights to improve muscle strength and endurance."
                subhead3 = "Balance and Stability"
                text3 = "Include exercises that improve balance and coordination, such as tai chi or yoga, to reduce the risk of falls and injuries."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the ovulation phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and lean proteins to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Engage in strength training exercises using resistance bands or light weights to build muscle mass and improve overall strength."
                subhead3 = "Appetite"
                text3 = "Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain and muscle growth."
    
    elif phase == 'luteal':
        if age_group == "teen":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, focus on consuming a balanced diet rich in fruits, vegetables, whole grains, and lean proteins to support weight loss goals and manage cravings."
                subhead2 = "Exercise"
                text2 = "Engage in moderate-intensity activities like brisk walking, swimming, or cycling to burn calories and reduce stress levels."
                subhead3 = "Stress Management"
                text3 = "Practice relaxation techniques such as deep breathing, meditation, or yoga to manage stress and emotional eating."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, prioritize protein-rich foods like eggs, poultry, fish, and legumes to support muscle repair and growth."
                subhead2 = "Exercise"
                text2 = "Incorporate strength training exercises using resistance bands or free weights to maintain muscle mass and improve overall strength."
                subhead3 = "Recovery"
                text3 = "Allow for adequate rest and recovery between workouts to prevent overtraining and promote muscle repair."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and whole milk to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Focus on compound exercises that target multiple muscle groups, such as squats, deadlifts, and bench presses, and gradually increase weights and volume to promote muscle growth."
                subhead3 = "Hydration"
                text3 = "Drink plenty of fluids to stay hydrated and support muscle recovery."
        elif age_group == "adult":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, emphasize portion control and choose nutrient-dense foods like fruits, vegetables, whole grains, and lean proteins to support weight loss efforts."
                subhead2 = "Exercise"
                text2 = "Incorporate a mix of cardio and strength training exercises to maximize calorie burn and preserve lean muscle mass."
                subhead3 = "Stress Management"
                text3 = "Practice stress-reducing activities like yoga, meditation, or spending time outdoors to manage stress and prevent emotional eating."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, aim for a balanced diet with adequate protein, carbohydrates, and healthy fats to fuel workouts and support muscle repair and growth."
                subhead2 = "Exercise"
                text2 = "Continue with your regular strength training routine, focusing on progressive overload and incorporating a variety of exercises to target different muscle groups."
                subhead3 = "Recovery"
                text3 = "Prioritize rest and recovery to allow your muscles to repair and grow stronger."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, increase calorie intake with nutrient-dense foods like lean meats, dairy, whole grains, and healthy fats to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Incorporate compound exercises that target multiple muscle groups, such as squats, deadlifts, and rows, and gradually increase weights and volume over time."
                subhead3 = "Hydration"
                text3 = "Drink plenty of fluids, including water and sports drinks, to stay hydrated and support muscle recovery."
        
        elif age_group == "old":
            if fitness_goal == "lose weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, focus on portion control and choose nutrient-rich foods like fruits, vegetables, whole grains, and lean proteins to support weight loss goals."
                subhead2 = "Exercise"
                text2 = "Engage in low-impact activities like walking, swimming, or yoga to burn calories and improve cardiovascular health."
                subhead3 = "Stress Management"
                text3 = "Practice stress-relieving activities such as meditation, deep breathing, or spending time with loved ones to manage stress and prevent emotional eating."
            elif fitness_goal == "gain strength":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, ensure adequate protein intake to support muscle repair and growth, and include healthy fats and carbohydrates for sustained energy."
                subhead2 = "Exercise"
                text2 = "Incorporate resistance training exercises using bodyweight, resistance bands, or light weights to improve muscle strength and endurance."
                subhead3 = "Recovery"
                text3 = "Allow for sufficient rest and recovery between workouts to prevent overtraining and promote muscle repair and growth."
            elif fitness_goal == "gain weight":
                subhead1 = "Nutrition"
                text1 = "During the luteal phase, increase calorie intake with nutrient-dense foods like nuts, seeds, avocados, and lean proteins to support weight gain goals."
                subhead2 = "Exercise"
                text2 = "Engage in strength training exercises using resistance bands or light weights to build muscle mass and improve overall strength."
                subhead3 = "Appetite"
                text3 = "Pay attention to hunger cues and eat regular, balanced meals and snacks to support weight gain and muscle growth."

    return subhead1, text1, subhead2, text2, subhead3, text3  # Returning all subheadings and text for old in luteal phase



    