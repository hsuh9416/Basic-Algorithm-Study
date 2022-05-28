package com.basicalgorithm.basic_algorithm_java.controller;

import com.basicalgorithm.basic_algorithm_java.domain.User;
import com.basicalgorithm.basic_algorithm_java.service.TrialTestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import io.swagger.annotations.*;

@RestController
@RequestMapping("trial")
@Api(tags = { "RUN AS TRIAL TEST" })
public class TrialTestController {

    @Autowired
    private TrialTestService trialTestService;


    @GetMapping(path="/runtTest")
    @ApiOperation(value = "Status checking test", notes = "Test as trial REST request to check operation status whether runs normally")
    @ApiResponses(value = { @ApiResponse(code = 200, message = "running normally"),
                            @ApiResponse( code = 400, message = "Bad Request"),
                            @ApiResponse( code = 500, message = "Internal Server Error") })
    public ResponseEntity<Object> runTest(){
            return trialTestService.runStatusChecking();
    }

    @GetMapping(path="/about")
    @ApiOperation(value = "Explain the purpose of developing", notes = "Explanation of the purpose of developing the application")
    @ApiResponses(value = { @ApiResponse(code = 200, message = "running normally"),
            @ApiResponse( code = 400, message = "Bad Request"),
            @ApiResponse( code = 500, message = "Internal Server Error") })
    public ResponseEntity<Object> about(){
        return trialTestService.runAbout();
    }

    @PostMapping(path="/greeting")
    @ApiOperation(value = "Simple post testing", notes = "Use Input parameter to complete greeting sentence.")
    @ApiResponses(value = { @ApiResponse(code = 200, message = "running normally"),
            @ApiResponse( code = 400, message = "Bad Request"),
            @ApiResponse( code = 500, message = "Internal Server Error") })
    public ResponseEntity<Object> greeting(@RequestBody User user) {
        return trialTestService.sendGreetingMsg(user);
    }
}
