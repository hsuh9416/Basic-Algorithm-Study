package com.basicalgorithm.basic_algorithm_java.service;

import org.springframework.stereotype.Service;
import java.util.Calendar;

@Service
public class CommonFunction {

    public Calendar getTodayInfo(){
        return Calendar.getInstance();
    }
    public String getDayOfWeek(Calendar today){
        return switch (today.get(Calendar.DAY_OF_WEEK)) {
            case 1 -> "Sunday";
            case 2 -> "Monday";
            case 3 -> "Tuesday";
            case 4 -> "Wednesday";
            case 5 -> "Thursday";
            case 6 -> "Friday";
            case 7 -> "Saturday";
            default -> "day";
        };
    }
}
