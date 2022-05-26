package com.basicalgorithm.exercise.trial;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class TrialController {

    @RequestMapping(value= "/trial", method = RequestMethod.GET)
    public String callTrial() {
        return "Hello! This is trial code to check application working!";
    }

}
