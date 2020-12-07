# AutoTest
AutoTest platform


测试平台主要做测试用例，测试任务，测试集，测试设备的管理。提交job以后会把执行表的标记设True，测试框架的server会轮询执行表，检测到标记位为True, 会拿到suite和device的信息，根据suite拿到case的信息，在user目录下递归创建jobid, suitename, casename的目录，把case的执行参数从数据表拿出来，测试的deviceip，等业务参数保存在casename目录下一个input.json文件，继承unittest.Testcase类二次开发的测试类会解析json文件，拿到业务参数，将结果写到用例结果表，在连表写到job 结果表。

To Do

前端页面和性能优化，测试框架server端代码在调试
