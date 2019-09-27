package com.ztocwst.stress.domain;

import java.util.*;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-07-01 11:08
 **/
public class ItemDTO {

    private String itemString;

    private String[] itemCode;

    private String[] itemName={"E 300H-2 单换气(后壳米白) 氧化银 300*300","E-JC-60BLHF 08 吹风+PTC+换气+照明+显示五合一(后壳灰色) 氧化银 300*600","D0033-D/14W/3000K(黑色)","D0005-X/36W/TR(白色)","D0041-X/24W/TR(原木色)"};

    public ItemDTO(String[] itemCode) {
        this.itemCode = itemCode;
    }
    public List<Map<String,Object>> list1(){
        List list=new ArrayList<>();
        Map<String,Object> map=new HashMap<>();
        map.put("itemCode","6927006122410");
        map.put("itemName","三生花 舒漾细肤沁透保湿喷雾70ml");
        map.put("number",5);
        Map<String,Object> map2=new HashMap<>();
        map2.put("itemCode","6927006122847");
        map2.put("itemName","三生花面膜 金盏花细致嫩肤面膜（5片装");
        map2.put("number",5);
        Map<String,Object> map3=new HashMap<>();
        map3.put("itemCode","TM11112700002");
        map3.put("itemName","wl百雀羚 水嫩柔滑夜间精华面膜(睡眠型) 3g");
        map3.put("number",5);
        list.add(map);
        list.add(map2);
        list.add(map3);
        return list;
    }

    public List<Map<String,Object>> list2(){
        List list=new ArrayList<>();
        Map<String,Object> map=new HashMap<>();
        map.put("itemCode","TM5187020190803");
        map.put("itemName","百雀羚 中秋节全店228礼包");
        map.put("number",4);
        Map<String,Object> map2=new HashMap<>();
        map2.put("itemCode","5187019070035");
        map2.put("itemName","百雀羚818热巴贴纸19年版（EC");
        map2.put("number",1);
        list.add(map);
        list.add(map2);
        return list;
    }

    public List<Map<String,Object>> list3(){
        List list=new ArrayList<>();
        Map<String,Object> map=new HashMap<>();
        map.put("itemCode","6927006124933");
        map.put("itemName","wl百雀羚 肌初赋活臻享体验套装（新版)");
        map.put("number",20);
        Map<String,Object> map2=new HashMap<>();
        map2.put("itemCode","6927006127606");
        map2.put("itemName","三生花 花媚尤物炫彩唇釉-BE01");
        map2.put("number",20);
        list.add(map);
        list.add(map2);
        return list;
    }




    public String getItemString() {

        List<Map<String,Object>> list = null;
        int num = (int) (Math.random() * 3 + 1);
        if(num == 1){
            list =  list1();
        }else if(num == 2){
            list =  list2();
        }else{
            list =  list3();
        }

        StringBuffer sb = new StringBuffer();
        for (int i =0; i< list.size(); i++) {
            int a = new Random().nextInt(itemCode.length);
                    sb.append( " <orderLine>\n" +
                    "      <actualPrice>86.0</actualPrice>\n" +
                    "      <discountPrice>0.0</discountPrice>\n" +
                    "      <inventoryType>ZP</inventoryType>\n" +
                    "      <itemCode>"+list.get(i).get("itemCode")+"</itemCode>\n" +
                    "      <itemId/>\n" +
                    "      <itemName>"+list.get(i).get("itemName")+"</itemName>\n" +
                    "      <orderLineNo>5</orderLineNo>\n" +
                    "      <ownerCode>CS0758</ownerCode>\n" +
                    "      <planQty>"+list.get(i).get("number")+"</planQty>\n" +
                    "      <produceCode>BMMBMM005</produceCode>\n" +
                    "      <retailPrice>43.0</retailPrice>\n" +
                    "      <sourceOrderCode>307286412821847607</sourceOrderCode>\n" +
                    "    </orderLine>");
        }

        return sb.toString();
    }

    public void setItemString(String itemString) {
        this.itemString = itemString;
    }


    public static void main(String[] args) {
        System.out.println(Math.random());
    }
}
