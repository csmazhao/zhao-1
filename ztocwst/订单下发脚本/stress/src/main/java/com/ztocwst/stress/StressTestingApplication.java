package com.ztocwst.stress;

import com.ztocwst.stress.task.SendTask;
import com.ztocwst.stress.task.SendTask1;
import com.ztocwst.stress.task.SendTask2;
import com.ztocwst.stress.task.StartMain;
import com.ztocwst.stress.util.SkuBjslItemCode;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@SpringBootApplication
public class StressTestingApplication {
    public static void main(String[] args) {
        SpringApplication.run(StressTestingApplication.class, args);
    }



}

