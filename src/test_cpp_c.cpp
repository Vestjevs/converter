int main()
{
    {
        auto hello = "Hello world";
        auto world = "world";

        {
            auto hello = "Hello world";
            auto world = "world";

            {
                auto hello = "Hello world";
                auto world = "world";
                auto flag = true && false;
                {
                    auto hello = "Hello world";
                    auto world = "world";
                }
            }
        }
        
    }
    auto hello = "Hello world";
    auto world = "world";
    return 0;
}