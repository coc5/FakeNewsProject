package com.example.FakeNews.controller;

import com.example.FakeNews.service.NewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.ui.Model;

import java.util.Map;

@Controller
public class NewsController {
    @GetMapping("/index")
    public String showIndex() {
        return "/WEB-INF/views/index";
    }
}
//@RequestMapping("/")
//public class NewsController {
//
//    @Autowired
//    private NewsService newsService;
//
//    @GetMapping
//    public String showIndex() {
//        return "index"; // index.jsp로 이동
//    }
//
//    // 뉴스 예측 요청 처리(결과를 result.jsp로 전달)
//    @PostMapping("/predict")
//    public String predictNews(@RequestParam String title,
//                              @RequestParam String content,
//                              Model model) {
//        String result = newsService.predictNews(title, content);
//        model.addAttribute("prediction", result);
//        return "result"; // JSP 파일 (result.jsp)으로 이동
//    }
//
//    // 뉴스 어노테이션 저장 후 리디렉션
//    @PostMapping("/annotate")
//    public String annotateNews(@RequestParam String title, @RequestParam String content, @RequestParam String label) {
//        newsService.saveAnnotation(title, content, label);
//        return "redirect:/index"; // 어노테이션 후 메인 페이지로 리디렉션
//    }
//}
