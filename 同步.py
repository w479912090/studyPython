#普通同步代码实现多个ID任务
import time
def taskIO_1():
    start = time.time()
    print('开始IO任务1...')
    time.sleep(2)
    print('IO任务1完成，耗时：%.5f秒' % float(time.time() - start))
def taskIO_2():
    start = time.time()
    print('开始IO任务2...')
    time.sleep(3)
    print('IO任务2完成，耗时：%.5f秒' % float(time.time() - start))

start = time.time()
taskIO_1()
taskIO_2()
print('所有IO任务完成耗时：%.5f秒' % float(time.time() - start))

#yield  和yield from
def generator_1(titles):
    yield titles
def generator_2(titles):
    yield from titles
    # 等价于
    # for title in titles:
    #     yield title

titles = ['Java', 'C++', 'Python']
for title in generator_1(titles):
    print('生成器1：', title)
for title in generator_2(titles):
    print('生成器2：', title)

#通过生成器来实现一个整数加和的程序
def generator_3():
    total = 0
    while True:
        x = yield
        print('+', x)
        if not x:
            break
        total += x
    print('tatal:', total)
    return total
def generator_4():  #委托生成器
    while True:
        total = yield from generator_3()    #子生成器
        print('total:', total)
def main():
    # g1 = generator_3()
    # g1.send(None)
    # g1.send(2)
    # g1.send(3)
    # g1.send(None)
    g2 = generator_4()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)

main()

#yield from在其中还有一个关键的作用是：建立调用方和子生成器的通道
#在上述代码中main()每一次在调用send(value)时，value不是传递给了委托生成器generator_2()，
#而是借助yield from传递给了子生成器generator_1()中的yield
#同理，子生成器中的数据也是通过yield直接发送到调用方main()中。