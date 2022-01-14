Kg=1; 
X0=1;
XP0=0;
Y0=0; 
YP0=1; 
T0=0; 
TN=10; 
dT=0.01; 
Planet1=@(t,z) [z(2); -Kg*z(1)./(z(1).^2+z(3).^2).^(3/2); z(4); -
Kg*z(3)./(z(1).^2+z(3).^2).^(3/2)]; 
[T,Y]=ode45(Planet1,[T0:dT:TN],[X0, XP0, Y0, YP0]); 
figure('Color',[1 1 1]);
hL1=plot(Y(:,1),Y(:,3),0,0); grid; 
set(hL1(1), 'LineWidth', 2, 'Color', 'b');
set(hL1(2), 'Marker', 'o', 'MarkerSize', 8, 'Color', 'r', 'MarkerFaceColor', 'r' );
ylabel('\ity','fontsize',14);
xlabel('\itx','fontsize',14);
title (sprintf('{\\itx}=%3.1f, {\\ity}=%3.1f, {\\itV}_x=%3.1f, {\\itV}_y=%3.1f ',X0,Y0,XP0,YP0),'fontsize',12);
