package com.ztocwst.stress.task;

import com.ztocwst.stress.domain.MessageDTO;
import com.ztocwst.stress.domain.MessageDTO1;
import com.ztocwst.stress.domain.MessageDTO2;
import com.ztocwst.stress.util.HttpUrlWmsRequest;
import org.apache.commons.lang3.time.StopWatch;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Date;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-06-25 14:18
 **/
public class SendTask2 implements  Runnable {
    private final static Logger logger = LoggerFactory.getLogger("runFlag");
   // private final static Logger logger1 = LoggerFactory.getLogger("runReturn");
   private Integer i;
    private String[] bjslcode;
    private String[] lszmcode;
    private Integer number;

    public SendTask2(Integer number,Integer i, String[] bjslcode, String[] lszmcode){
        this.number = number;
        this.i = i;
        this.bjslcode = bjslcode;
        this.lszmcode = lszmcode;
    }

    @Override
    public void run() {
        long id = Thread.currentThread().getId();
        StopWatch sw = new StopWatch();
        sw.start();
        String info = null;
        //奇数发一个货主，偶数再发另外一个货主
        MessageDTO2 messageDTO = new MessageDTO2(number,lszmcode);
        messageDTO.setNo(""+new Date().getTime() + i);
        try {
            info = HttpUrlWmsRequest.sendPostQiMen(messageDTO.getUrl(),messageDTO.getBody());
            logger.info("threadId:{}=======run散包========",id);
            logger.info("Time:{},threadId:{}=========返回:{}===========",sw,id,info);
        } catch (Exception e) {
            logger.info("=========runExcption=============");
            logger.info("============Message==========" + e.getMessage());
            e.printStackTrace();
        }
        sw.stop();


//        long id = Thread.currentThread().getId();
//        StopWatch sw = new StopWatch();
//        sw.start();
//        String info = null;
//        //奇数发一个货主，偶数再发另外一个货主
//        if(i%2 == 0){
//            send(id, sw);
//
//        }else{
//            send(id, sw);
//        }



        //System.out.println("耗时"+sw+"毫秒，返回:"+info);
    }

    private void send(long id, StopWatch sw) {
        String info;
        try {
            MessageDTO messageDTO = new MessageDTO(lszmcode);
            messageDTO.setNo("" + new Date().getTime() + i);
            info = HttpUrlWmsRequest.sendPostQiMen(messageDTO.getUrl(), messageDTO.getBody());
            logger.info("threadId:{}=======run========", id);
            logger.info("Time:{},threadId:{}=========返回:{}===========", sw, id, info);
        } catch (IOException e) {
            logger.info("=========runExcption=============");
            logger.info("============Message==========" + e.getMessage());
            e.printStackTrace();
        }
    }
}
