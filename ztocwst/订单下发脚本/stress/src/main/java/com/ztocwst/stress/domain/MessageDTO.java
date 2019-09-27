package com.ztocwst.stress.domain;

import org.apache.commons.lang3.RandomStringUtils;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.util.Calendar;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-06-25 13:53
 **/
public class MessageDTO {

    private String body;

    private String url="http://qimen.pet.ztocwst.com/api/edi/qimen/in?method=deliveryorder.create&timestamp=2018-11-21%3000:00:00&format=xml&app_key&v=1.0&sign&sign_method=md5&customerId=CS0758";

    private String no;


    private String[] code;

    public MessageDTO(String[] code) {
        this.code = code;
    }

    public String getBody() {
        String rStr =  System.nanoTime()+"";
        String str = rStr.substring(rStr.length() - 6);

        String time = RandomStringUtils.randomAlphanumeric(32);
        ItemDTO itemDTO = new ItemDTO(code);
        body = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n" +
                "<request>\n" +
                "  <deliveryOrder>\n" +
                "    <arAmount>0.0</arAmount>\n" +
                "    <buyerMessage/>\n" +
                "    <buyerNick>刘瑞</buyerNick>\n" +
                "    <createTime>2019-06-25 13:57:17</createTime>\n" +
                "    <deliveryOrderCode>CWST"+getNo()+"</deliveryOrderCode>\n" +
                "    <extendProps>\n" +
                "      <key1>null</key1>\n" +
                "      <routeCode>null</routeCode>\n" +
                "      <key2>null</key2>\n" +
                "      <isThreePL>N</isThreePL>\n" +
                "      <key3>null</key3>\n" +
                "      <isJitx>false</isJitx>\n" +
                "      <vendorId>null</vendorId>\n" +
                "      <shopId>null</shopId>\n" +
                "      <storeCode>tb_bmhtqjd</storeCode>\n" +
                "    </extendProps>\n" +
                "    <freight>0.0</freight>\n" +
                "    <gotAmount>135.0</gotAmount>\n" +
                "    <invoiceFlag>N</invoiceFlag>\n" +
                "    <isUrgency>N</isUrgency>\n" +
                "    <itemAmount>135.0</itemAmount>\n" +
                "    <logisticsCode>CWST-TEST</logisticsCode>\n" +
                "    <logisticsName>中通快递</logisticsName>\n" +
                "    <expressCode>"+getNo()+"</expressCode> "+
                "    <operateTime>2019-06-25 13:57:17</operateTime>\n" +
                "    <orderFlag/>\n" +
                "    <orderType>JYCK</orderType>\n" +
                "    <ownerCode>CS0758</ownerCode>\n" +
                "    <payTime>2019-08-30 13:42:15</payTime>\n" +
                "    <placeOrderTime>2019-06-25 13:57:17</placeOrderTime>\n" +
                "    <receiverInfo>\n" +
                "      <area>余杭区</area>\n" +
                "      <city>杭州市</city>\n" +
                "      <countryCode>1</countryCode>\n" +
                "      <detailAddress>浙江省 杭州市 余杭区 未来科技城研创园520室</detailAddress>\n" +
                "      <mobile>18158685663</mobile>\n" +
                "      <name>刘瑞</name>\n" +
                "      <province>浙江省</province>\n" +
                "      <zipCode>310012</zipCode>\n" +
                "    </receiverInfo>\n" +
                "    <remark/>\n" +
                "    <sellerMessage/>\n" +
                "    <sellerNick>百雀羚</sellerNick>\n" +
                "    <senderInfo>\n" +
                "      <area>花都区</area>\n" +
                "      <city>广州市</city>\n" +
                "      <countryCode>CN</countryCode>\n" +
                "      <detailAddress>广州市花山镇起源大道14号中通花山分拨中心</detailAddress>\n" +
                "      <name>1</name>\n" +
                "      <province>广东省</province>\n" +
                "    </senderInfo>\n" +
                "    <shopNick> </shopNick>\n" +
                "    <sourcePlatformCode>TM</sourcePlatformCode>\n" +
                "    <sourcePlatformName>TMALL</sourcePlatformName>\n" +
                "    <totalAmount>135.0</totalAmount>\n" +
                "    <warehouseCode>010-002C</warehouseCode>\n" +
                "  </deliveryOrder>\n" +
                "  <orderLines>\n" +
                itemDTO.getItemString()+
                "  </orderLines>\n" +
                "</request>";
//        body.replace("<deliveryOrderCode>CWST</deliveryOrderCode>","<deliveryOrderCode>CWST20190625"+no+"</deliveryOrderCode>");
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public static String getNo() {
        String  num =   Calendar.getInstance().getTimeInMillis() + "" +  ((long)(Math.random()*(99999l - 10000l)) + 10000l) + "";
        return num;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setNo(String no) {
        this.no = no;
    }
}
