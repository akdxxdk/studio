#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : studio
# @FileName  :chatgpt4.py
# @Time      :2023/4/24 22:19
# @Author    :和孔哥一起学
# @Email     :2338199895@qq.com
# @CSDN and Public      :和孔哥一起学

from steamship import Steamship

if __name__ == "__main__":
    # Create a Steamship client
    # NOTE: When developing a package, just use `self.client`
    client = Steamship(workspace="gpt-4-2g0")

    # Create an instance of this generator
    generator = client.use_plugin('gpt-4')

    # Generate text
    task = generator.generate(text="写一份Python基础课总结报告，字数五千字。")

    # Wait for completion of the task.
    task.wait()

    # Print the output
    print(task.output.blocks[0].text)
