package com.ztocwst.stress.task;

import com.ztocwst.stress.util.SkuBjslItemCode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import java.text.ParseException;
import java.util.concurrent.Executor;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-06-25 13:49
 **/
@Component
@Scope("prototype")
public class StartMain1 {
    private final static Logger logger = LoggerFactory.getLogger("runFlag");
    @Qualifier("taskExecutor1")
    @Autowired
    private  Executor taskExecutor1;
    private boolean flag = true;
    String[] bjslcode = new SkuBjslItemCode().readTxtFile("sku_BJSL001.txt");
    String[] lszmcode = new SkuBjslItemCode().readTxtFile("itemCode.txt");
    @Bean
    public  void start1() throws ParseException {
        //每隔1秒钟创建150个线程
        //A
//        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
//        String dateStr = format.format(new Date());
//        format.setTimeZone(TimeZone.getTimeZone("GMT+0"));
//        Date date = format.parse(dateStr);
//        format.setTimeZone(TimeZone.getTimeZone("GMT+2"));
//        dateStr = format.format(date);

        int count250 = 0;
        int count150 = 0;
        int count100 = 0;
        while (flag)
            //250万
//            if (count250 <= 1) {
//                for (int i = 0; i < 1; i++) {
//                    taskExecutor.execute(new SendTask(i, bjslcode, lszmcode));
//                }
//                count250++;
//            }
//
//            //150万
//             if (count150 <= 1650) {
//                for (int i = 0; i < 500; i++) {
//                    taskExecutor1.execute(new SendTask1(i, bjslcode, lszmcode));
//                }
//                count150++;
//            }

//            //100万
//            if (count150 <= 850) {
//                for (int i = 0; i < 500; i++) {
//                    taskExecutor2.execute(new SendTask2(i, bjslcode, lszmcode));
//                }
//                count100++;
//            }

            try {
                Thread.sleep(950L);
            } catch (InterruptedException e) {

            }
        }

}



