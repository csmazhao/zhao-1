package com.ztocwst.stress.util;/**
 * @Author: mulan
 * @Date: 2018/12/27 19:46
 * @Version 1.0
 */

import com.github.shyiko.mysql.binlog.BinaryLogFileReader;
import com.github.shyiko.mysql.binlog.event.Event;
import com.github.shyiko.mysql.binlog.event.deserialization.ChecksumType;
import com.github.shyiko.mysql.binlog.event.deserialization.EventDeserializer;

import java.io.File;
import java.io.IOException;

/**
 * @version v1.0
 * @program: zyouth-biz-parent
 * @description:
 * @author: Administrator
 * @create: 2018-12-27 19:46
 **/
public class Test
{

    /**
     * <dependency>
     * 			<groupId>com.github.shyiko</groupId>
     * 			<artifactId>mysql-binlog-connector-java</artifactId>
     * 			<version>0.13.0</version>
     * 		</dependency>
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        String filePath="F:\\日志\\3-19\\3-19\\mysql-bin.000741";
        File binlogFile = new File(filePath);
        EventDeserializer eventDeserializer = new EventDeserializer();
        eventDeserializer.setChecksumType(ChecksumType.CRC32);
        BinaryLogFileReader reader = new BinaryLogFileReader(binlogFile, eventDeserializer);

        try {
            int i =0;
            for (Event event; (event = reader.readEvent()) != null; ) {
//                if (event.getHeader().getEventType() == EventType.) {
                    String s = event.toString();
//                    if ((s.contains("tableId=610") && s.contains("981129631611020006")) || (s.contains("tableId=2516") && s.contains("GZTB1C"))) {
//                    if (s.contains("2018-12-24 11") && s.contains("tableId=2516") && s.contains("GZTB1C")){
//                    if ( s.contains("1550833929000") ){
//                if (s.contains("JY19071818270")){

                        System.out.println(event.toString());
                        i++;


//                    }

//                if (event.getHeader().getTimestamp()> 1551157836000L &&  event.getHeader().getTimestamp() <1551158436000L && !s.contains("maxwell")){
//                    System.out.println(event.toString());
//                }
//                if (i == 30){
//                        break;
//                }
                }


//            }
        } finally {
            reader.close();
        }

//        981128631659020006
//        981128631634020006


    }
}
