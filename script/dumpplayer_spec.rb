require 'gema'

describe Gema::DumbPlayer do
before :each do
@dp = Gema::DumbPlayer.new("X")
end

it "Debe existir un metodo move" do
@dp.respond_to?("move").should == true
end

end
