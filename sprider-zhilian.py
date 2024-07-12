import re
import time

import requests
from bs4 import BeautifulSoup


class Spriderr:
    def __init__(self):
        # 城市
        self.city = ['北京', '上海', '广州', '深圳', '天津', '武汉', '成都', '杭州']
        # 需要获取的关键字
        self.words = ['职位名称', '公司名称', '薪资', '工作城市', '工作经验', '学历要求', '企业类型']
        # 搜索关键字
        self.keyword_job = '人力'
        # 需要爬取的数量
        self.num = 200

    def get_data(self, city, keyword_job, page) -> requests:
        data = requests.get(f'https://sou.zhaopin.com/?kw={keyword_job}&jl={city}&p={page}')
        return data

    def down_dim(self, list_: list) -> list:
        """
        数组降维
        :rtype: list;
        """
        list_ = [item for sublist in list_ for item in sublist]
        return list_

    def get_analysis(self, data: str) -> list:
        """解析出职位"""
        analysis = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('div.jobinfo__top a')
        for tag in tag:
            analysis.append(tag.string)
        return analysis

    def get_company(self, data: str):
        """解析出公司"""
        company = []
        bs = BeautifulSoup(data, features='html.parser')
        tag = bs.select('a.companyinfo__name')
        for tag in tag:
            string = re.sub(r'\s', '', tag.string)
            company.append(string)
        return company

    def get_salary(self, data: str):
        """解析出薪资"""
        company = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('p.jobinfo__salary')
        for tag in tag:
            string = re.sub(r'\s', '', tag.string)
            company.append(string)
        return company

    def get_city(self, data: str) -> list:

        """解析出城市"""
        city = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('div.jobinfo__other-info-item:nth-child(1) > span')
        for tag in tag:
            city.append(tag.string)
        return city

    def get_experience(self, data: str):
        """解析出经验"""
        exp = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('div.jobinfo__other-info-item:nth-child(2)')
        for tag in tag:
            string = re.sub(r'\s', '', tag.string)
            exp.append(string)
        return exp

    def get_education(self, data: str):
        """解析出学历"""
        education = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('div.jobinfo__other-info > div:nth-child(3)')
        for tag in tag:
            string = re.sub(r'\s', '', tag.string)
            education.append(string)
        return education

    def get_enterprisetype(self, data: str):
        """解析出企业类型"""
        enterprisetype = []
        bs = BeautifulSoup(data, 'lxml')
        tag = bs.select('div.companyinfo__tag > div:nth-child(1)')
        for tag in tag:
            string = re.sub(r'\s', '', tag.string)
            enterprisetype.append(string)
        return enterprisetype

    def run(self):
        citys = []
        analysis_list = []
        company_list = []
        salary_list = []
        city_list = []
        experience_list = []
        education_list = []
        enterprisetype_list = []
        for city in self.city:
            for i in range(20):
                citys.append(city)
            web = self.get_data(city=city, keyword_job=self.keyword_job, page=1)
            analysis_list.append(self.get_analysis(web.text))
            company_list.append(self.get_company(web.text))
            salary_list.append(self.get_salary(web.text))
            city_list.append(self.get_city(web.text))
            experience_list.append(self.get_experience(web.text))
            education_list.append(self.get_education(web.text))
            enterprisetype_list.append(self.get_enterprisetype(web.text))
        analysis_list = self.down_dim(analysis_list)
        company_list = self.down_dim(company_list)
        salary_list = self.down_dim(salary_list)
        city_list = self.down_dim(city_list)
        experience_list = self.down_dim(experience_list)
        education_list = self.down_dim(education_list)
        enterprisetype_list = self.down_dim(enterprisetype_list)
        with open('data.txt', 'w', encoding='utf-8') as file:
            for i in range(len(city_list)):
                file.write(
                    f'{citys[i]}|{analysis_list[i]}|{company_list[i]}|{salary_list[i]}|{city_list[i]}|{experience_list[i]}|{education_list[i]}|{enterprisetype_list[i]}\n')

        print("Data written to data.txt")

        time.sleep(3)

    # def run(self, page):
    #     for city in self.city:
    #         for i in range(20):
    #             data = requests.get(f'https://sou.zhaopin.com/?kw={self.keyword_job}&jl={city}&p=1')
    #             bs = BeautifulSoup(data, 'lxml')
    #             analysis = bs.select('div.companyinfo__tag > div:nth-child(1)')
    #             for tag in tag:
    #                 string = re.sub(r'\s', '', tag.string)
    #                 enterprisetype.append(string)


if __name__ == '__main__':
    spider = Spriderr()
    spider.run()
